"""Feature extraction: a frozen pretrained model turns text into a vector."""

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from transformers import AutoModel, AutoTokenizer

from baselines import scores

MODEL = "distilbert/distilbert-base-uncased"


@torch.no_grad()
def embed_texts(texts, model_name=MODEL, batch_size=32, max_length=64):
    """Mean of the last hidden states over the real tokens, one row per text."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).eval()
    rows = []
    for start in range(0, len(texts), batch_size):
        batch = tokenizer(
            texts[start : start + batch_size],
            padding=True,
            truncation=True,
            max_length=max_length,
            return_tensors="pt",
        )
        hidden = model(**batch).last_hidden_state
        mask = batch["attention_mask"].unsqueeze(-1)
        rows.append(((hidden * mask).sum(1) / mask.sum(1)).numpy())
    return np.vstack(rows)


def frozen_features_baseline(train_texts, train_labels, eval_texts, eval_labels):
    """Logistic regression on frozen embeddings: nothing in the model is trained."""
    clf = LogisticRegression(max_iter=2000)
    clf.fit(embed_texts(train_texts), train_labels)
    return scores(eval_labels, clf.predict(embed_texts(eval_texts)))
