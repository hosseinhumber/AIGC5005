"""Fine-tune a pretrained model with a training loop you can read."""

import time

import torch
from torch.utils.data import DataLoader
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    DataCollatorWithPadding,
    get_linear_schedule_with_warmup,
    set_seed,
)

from baselines import scores

MODEL = "distilbert/distilbert-base-uncased"
ID2LABEL = {0: "negative", 1: "positive"}


def encode(tokenizer, texts, labels, max_length=64):
    """One dictionary per text, without padding. The collator pads each batch."""
    enc = tokenizer(texts, truncation=True, max_length=max_length)
    return [
        {"input_ids": enc["input_ids"][i],
         "attention_mask": enc["attention_mask"][i],
         "labels": labels[i]}
        for i in range(len(texts))
    ]  # fmt: skip


def make_loader(tokenizer, texts, labels, batch_size, shuffle, seed=42):
    generator = torch.Generator().manual_seed(seed)
    return DataLoader(
        encode(tokenizer, texts, labels),
        batch_size=batch_size,
        shuffle=shuffle,
        generator=generator if shuffle else None,
        collate_fn=DataCollatorWithPadding(tokenizer),
    )


def freeze_body(model) -> int:
    """Stop the pretrained layers learning. Returns the trainable parameter count."""
    for parameter in model.distilbert.parameters():
        parameter.requires_grad = False
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


@torch.no_grad()
def predict(model, loader) -> list[int]:
    model.eval()
    out = []
    for batch in loader:
        batch = {k: v for k, v in batch.items() if k != "labels"}
        out += model(**batch).logits.argmax(dim=-1).tolist()
    return out


def fine_tune(
    train_texts,
    train_labels,
    val_texts,
    val_labels,
    head_only=False,
    epochs=3,
    lr=5e-5,
    batch_size=16,
    seed=42,
    model_name=MODEL,
):
    """Train, log every epoch, and return the model, the tokenizer and the history."""
    set_seed(seed)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        model_name, num_labels=2, id2label=ID2LABEL,
        label2id={v: k for k, v in ID2LABEL.items()},
    )  # fmt: skip
    if head_only:
        freeze_body(model)
    train_loader = make_loader(
        tokenizer, train_texts, train_labels, batch_size, True, seed
    )
    val_loader = make_loader(tokenizer, val_texts, val_labels, 64, False)
    optimizer = torch.optim.AdamW(
        [p for p in model.parameters() if p.requires_grad], lr=lr, weight_decay=0.01
    )
    total = epochs * len(train_loader)
    schedule = get_linear_schedule_with_warmup(optimizer, int(0.1 * total), total)
    history = []
    for epoch in range(1, epochs + 1):
        started = time.perf_counter()
        model.train()
        running = 0.0
        for batch in train_loader:
            loss = model(**batch).loss
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            schedule.step()
            optimizer.zero_grad()
            running += loss.item()
        result = scores(val_labels, predict(model, val_loader))
        history.append(
            {"epoch": epoch,
             "train_loss": round(running / len(train_loader), 4),
             "val_accuracy": result["accuracy"],
             "val_macro_f1": result["macro_f1"],
             "seconds": round(time.perf_counter() - started, 1)}
        )  # fmt: skip
    return model, tokenizer, history


def evaluate(model, tokenizer, texts, labels) -> dict[str, float]:
    loader = make_loader(tokenizer, texts, labels, 64, False)
    return scores(labels, predict(model, loader))
