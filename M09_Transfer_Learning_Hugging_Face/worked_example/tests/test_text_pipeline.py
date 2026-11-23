import numpy as np
import pytest
import torch

from embed import embed_texts
from finetune import encode, make_loader
from review_data import LABELS, small_sample


def test_tokenizer_adds_special_tokens_and_lowercases(tokenizer):
    ids = tokenizer("Great Movie")["input_ids"]
    tokens = tokenizer.convert_ids_to_tokens(ids)
    assert tokens == ["[CLS]", "great", "movie", "[SEP]"]


def test_padding_gives_equal_lengths_and_a_mask(tokenizer):
    batch = tokenizer(["fine", "a much longer sentence here"], padding=True)
    assert len(set(map(len, batch["input_ids"]))) == 1
    assert batch["attention_mask"][0][-1] == 0
    assert sum(batch["attention_mask"][1]) == len(batch["input_ids"][1])


@pytest.mark.parametrize("limit", [4, 8, 16])
def test_truncation_respects_the_limit(tokenizer, limit):
    text = "this sentence has far more words than the limit allows " * 3
    ids = tokenizer(text, truncation=True, max_length=limit)["input_ids"]
    assert len(ids) == limit


def test_encode_keeps_labels_and_leaves_padding_to_the_collator(tokenizer):
    rows = encode(tokenizer, ["short", "a slightly longer one"], [0, 1])
    assert [r["labels"] for r in rows] == [0, 1]
    assert len(rows[0]["input_ids"]) < len(rows[1]["input_ids"])
    loader = make_loader(
        tokenizer, ["short", "a slightly longer one"], [0, 1], 2, False
    )
    batch = next(iter(loader))
    assert batch["input_ids"].shape[0] == 2
    assert batch["labels"].dtype == torch.long


def test_small_sample_is_balanced_and_repeatable(reviews):
    texts, labels = small_sample(reviews["train"], 40, seed=1)
    assert len(texts) == 40 and sum(labels) == 20
    again, _ = small_sample(reviews["train"], 40, seed=1)
    assert texts == again
    assert LABELS == ["negative", "positive"]


def test_validation_and_train_sentences_do_not_overlap(reviews):
    train = set(reviews["train"]["text"])
    assert not train & set(reviews["validation"]["text"])


def test_embedding_ignores_padding():
    short = "good"
    long = "a very much longer sentence that forces padding on the short one"
    alone = embed_texts([short], batch_size=1)
    together = embed_texts([short, long], batch_size=2)
    assert alone.shape == (1, 768)
    assert np.allclose(alone[0], together[0], atol=1e-3)
