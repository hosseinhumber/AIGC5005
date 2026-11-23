"""A classical baseline: word counts and logistic regression."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.pipeline import make_pipeline


def scores(labels, predicted) -> dict[str, float]:
    return {
        "accuracy": round(float(accuracy_score(labels, predicted)), 4),
        "macro_f1": round(float(f1_score(labels, predicted, average="macro")), 4),
    }


def tfidf_baseline(train_texts, train_labels, eval_texts, eval_labels):
    """Fit on the training texts only and score on the evaluation texts."""
    model = make_pipeline(
        TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True),
        LogisticRegression(C=10, max_iter=1000),
    )
    model.fit(train_texts, train_labels)
    return scores(eval_labels, model.predict(eval_texts))
