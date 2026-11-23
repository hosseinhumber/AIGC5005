"""The same fine-tuning with the Trainer class, which runs the loop for you."""

import numpy as np
from datasets import Dataset
from sklearn.metrics import accuracy_score, f1_score
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
    set_seed,
)

from finetune import ID2LABEL, MODEL


def compute_metrics(eval_prediction):
    logits, labels = eval_prediction
    predicted = np.argmax(logits, axis=-1)
    return {
        "accuracy": float(accuracy_score(labels, predicted)),
        "macro_f1": float(f1_score(labels, predicted, average="macro")),
    }


def fine_tune_with_trainer(
    train_texts,
    train_labels,
    val_texts,
    val_labels,
    epochs=3,
    lr=5e-5,
    batch_size=16,
    seed=42,
    output_dir="trainer_output",
    model_name=MODEL,
):
    set_seed(seed)  # before the model is created, so the new head is seeded too
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    def prepare(texts, labels):
        data = Dataset.from_dict({"text": texts, "label": labels})
        return data.map(
            lambda row: tokenizer(row["text"], truncation=True, max_length=64),
            batched=True,
            remove_columns=["text"],
        )

    model = AutoModelForSequenceClassification.from_pretrained(
        model_name, num_labels=2, id2label=ID2LABEL,
        label2id={v: k for k, v in ID2LABEL.items()},
    )  # fmt: skip
    args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=epochs,
        learning_rate=lr,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=64,
        weight_decay=0.01,
        warmup_steps=0.1,
        eval_strategy="epoch",
        save_strategy="no",
        logging_strategy="epoch",
        report_to="none",
        disable_tqdm=True,
        seed=seed,
    )
    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=prepare(train_texts, train_labels),
        eval_dataset=prepare(val_texts, val_labels),
        data_collator=DataCollatorWithPadding(tokenizer),
        compute_metrics=compute_metrics,
    )
    trainer.train()
    return trainer, tokenizer
