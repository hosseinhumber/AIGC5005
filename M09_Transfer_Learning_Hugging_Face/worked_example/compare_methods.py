"""Four approaches on 500 labelled reviews. Choose on validation, test once."""

import json
import sys

from sklearn.linear_model import LogisticRegression

from baselines import scores, tfidf_baseline
from embed import embed_texts
from finetune import evaluate, fine_tune
from review_data import as_lists, load_reviews, small_sample

N = 500


def main(seed: int = 42, score_test: bool = True) -> None:
    reviews = load_reviews()
    train_texts, train_labels = small_sample(reviews["train"], N, seed)
    val_texts, val_labels = as_lists(reviews["validation"])
    test_texts, test_labels = as_lists(reviews["test"])

    validation = {
        "tfidf": tfidf_baseline(train_texts, train_labels, val_texts, val_labels)
    }
    clf = LogisticRegression(max_iter=2000).fit(embed_texts(train_texts), train_labels)
    validation["frozen features"] = scores(
        val_labels, clf.predict(embed_texts(val_texts))
    )
    models = {}
    for name, head_only, lr in (
        ("head only", True, 1e-3),
        ("full fine-tune", False, 5e-5),
    ):
        model, tokenizer, history = fine_tune(
            train_texts, train_labels, val_texts, val_labels,
            head_only=head_only, lr=lr, seed=seed,
        )  # fmt: skip
        models[name] = (model, tokenizer)
        validation[name] = history[-1] | {"accuracy": history[-1]["val_accuracy"]}
        print(name, history[-1], flush=True)
    for name, result in validation.items():
        print(f"{name:16s} validation accuracy {result['accuracy']:.4f}")

    best = max(validation, key=lambda name: validation[name]["accuracy"])
    if not score_test:
        report = {
            "n": N,
            "seed": seed,
            "chosen": best,
            "validation": {k: v["accuracy"] for k, v in validation.items()},
        }
        with open(f"worked_metrics_seed{seed}.json", "w") as f:
            json.dump(report, f, indent=2)
        print("validation only, seed", seed, "| best:", best)
        return
    if best == "tfidf":
        test = tfidf_baseline(train_texts, train_labels, test_texts, test_labels)
    elif best == "frozen features":
        test = scores(test_labels, clf.predict(embed_texts(test_texts)))
    else:
        model, tokenizer = models[best]
        test = evaluate(model, tokenizer, test_texts, test_labels)
    print("chosen on validation:", best, "| test scored once:", test)
    report = {
        "n": N,
        "seed": seed,
        "chosen": best,
        "test": test,
        "validation": {k: v["accuracy"] for k, v in validation.items()},
    }
    with open(f"worked_metrics_seed{seed}.json", "w") as f:
        json.dump(report, f, indent=2)


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 42
    main(seed, score_test="--validation-only" not in sys.argv)
