import pytest
import torch
from transformers import AutoModelForSequenceClassification

from finetune import MODEL, evaluate, fine_tune, freeze_body
from review_data import as_lists, small_sample
from share import label_scores, load_classifier, save_model


@pytest.fixture(scope="module")
def tiny(reviews):
    texts, labels = small_sample(reviews["train"], 32, seed=0)
    val_texts, val_labels = as_lists(reviews["validation"].select(range(32)))
    return texts, labels, val_texts, val_labels


def test_freezing_leaves_only_the_head_trainable():
    model = AutoModelForSequenceClassification.from_pretrained(MODEL, num_labels=2)
    trainable = freeze_body(model)
    assert trainable == 768 * 768 + 768 + 768 * 2 + 2
    assert all(not p.requires_grad for p in model.distilbert.parameters())


def test_head_only_training_leaves_the_body_unchanged(tiny):
    before = AutoModelForSequenceClassification.from_pretrained(MODEL, num_labels=2)
    model, _, _ = fine_tune(*tiny, head_only=True, epochs=1, lr=1e-3)
    a = before.distilbert.embeddings.word_embeddings.weight
    b = model.distilbert.embeddings.word_embeddings.weight
    assert torch.equal(a, b)


def test_full_fine_tuning_changes_the_body(tiny):
    before = AutoModelForSequenceClassification.from_pretrained(MODEL, num_labels=2)
    model, _, _ = fine_tune(*tiny, epochs=1)
    a = before.distilbert.transformer.layer[5].ffn.lin1.weight
    b = model.distilbert.transformer.layer[5].ffn.lin1.weight
    assert not torch.equal(a, b)


def test_history_has_one_row_per_epoch(tiny):
    _, _, history = fine_tune(*tiny, epochs=2)
    assert [row["epoch"] for row in history] == [1, 2]
    assert {"train_loss", "val_accuracy", "val_macro_f1"} <= history[0].keys()


def test_same_seed_repeats_the_run(tiny):
    first = fine_tune(*tiny, epochs=1, seed=3)[2][0]["train_loss"]
    second = fine_tune(*tiny, epochs=1, seed=3)[2][0]["train_loss"]
    assert first == second


def test_can_memorize_a_small_batch(tiny):
    texts, labels, val_texts, val_labels = tiny
    model, tok, history = fine_tune(
        texts[:16], labels[:16], texts[:16], labels[:16], epochs=8, lr=5e-5
    )
    assert evaluate(model, tok, texts[:16], labels[:16])["accuracy"] >= 0.95


def test_a_saved_model_loads_and_predicts_the_same(tiny, tmp_path):
    model, tok, _ = fine_tune(*tiny, epochs=1)
    folder = save_model(model, tok, tmp_path / "model")
    classifier = load_classifier(folder)
    text = "a warm and funny film"
    scores = label_scores(classifier, text)
    assert set(scores) == {"negative", "positive"}
    assert sum(scores.values()) == pytest.approx(1.0, abs=1e-4)
    batch = tok(text, return_tensors="pt")
    with torch.no_grad():
        logits = model.eval()(**batch).logits[0]
    expected = torch.softmax(logits, -1)[1].item()
    assert scores["positive"] == pytest.approx(expected, abs=1e-4)
