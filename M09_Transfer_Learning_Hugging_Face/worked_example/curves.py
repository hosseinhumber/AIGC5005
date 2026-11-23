"""How much labelled data does each approach need? Four methods, growing samples."""

import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402

from baselines import scores, tfidf_baseline  # noqa: E402
from embed import embed_texts  # noqa: E402
from finetune import evaluate, fine_tune  # noqa: E402
from review_data import as_lists, load_reviews, small_sample  # noqa: E402

SIZES = (50, 100, 200, 500, 1000)
METHODS = ("tfidf", "frozen features", "head only", "full fine-tune")


def run(sizes=SIZES, seed=42, epochs=3, out="small_data_results.csv"):
    reviews = load_reviews()
    val_texts, val_labels = as_lists(reviews["validation"])
    val_vectors = embed_texts(val_texts)
    rows = []
    for n in sizes:
        texts, labels = small_sample(reviews["train"], n, seed)
        results = {"tfidf": tfidf_baseline(texts, labels, val_texts, val_labels)}
        clf = LogisticRegression(max_iter=2000).fit(embed_texts(texts), labels)
        results["frozen features"] = scores(val_labels, clf.predict(val_vectors))
        for name, head_only, lr in (
            ("head only", True, 1e-3),
            ("full fine-tune", False, 5e-5),
        ):
            model, tok, _ = fine_tune(
                texts, labels, val_texts, val_labels,
                head_only=head_only, epochs=epochs, lr=lr, seed=seed,
            )  # fmt: skip
            results[name] = evaluate(model, tok, val_texts, val_labels)
        for method, result in results.items():
            rows.append({"n": n, "seed": seed, "method": method, **result})
            print(n, method, result, flush=True)
    table = pd.DataFrame(rows)
    table.to_csv(out, index=False)
    return table


def plot(table, path="small_data_curves.png"):
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    for method in METHODS:
        part = table[table.method == method]
        ax.plot(part["n"], part["accuracy"], marker="o", label=method)
    ax.set_xscale("log")
    ax.set_xlabel("labelled training examples")
    ax.set_ylabel("validation accuracy")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 42
    table = run(seed=seed, out=f"small_data_results_seed{seed}.csv")
    plot(table, f"small_data_curves_seed{seed}.png")
