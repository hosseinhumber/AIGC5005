"""Train, check and save a churn model. Run it with:  python churn_model.py"""

import json
from pathlib import Path

import joblib
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from customers import make_customers

SEED = 42
NUMERIC = ["tenure_months", "monthly_charge", "support_calls"]
CATEGORICAL = ["contract", "payment"]


def build_pipeline() -> Pipeline:
    """Preprocessing and model in one object, so they are fitted and saved together."""
    preprocess = ColumnTransformer([
        ("num", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), NUMERIC),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAL),
    ])
    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    return Pipeline([("prep", preprocess), ("model", model)])


def evaluate(pipe: Pipeline, X, y) -> dict[str, float]:
    """Precision, recall, F1 and ROC-AUC for the churn class."""
    predicted = pipe.predict(X)
    probability = pipe.predict_proba(X)[:, 1]
    return {
        "precision": round(precision_score(y, predicted), 3),
        "recall": round(recall_score(y, predicted), 3),
        "f1": round(f1_score(y, predicted), 3),
        "roc_auc": round(roc_auc_score(y, probability), 3),
    }


def main() -> None:
    customers = make_customers(seed=SEED)
    X, y = customers.drop(columns="churned"), customers["churned"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=SEED
    )

    pipe = build_pipeline()
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    cv_f1 = cross_val_score(pipe, X_train, y_train, cv=folds, scoring="f1")
    print(f"Cross-validated F1 on the training data: {cv_f1.mean():.3f} +/- {cv_f1.std():.3f}")

    pipe.fit(X_train, y_train)
    test_scores = evaluate(pipe, X_test, y_test)
    print("Test set, used once:", test_scores)

    joblib.dump(pipe, "churn_model.joblib")
    record = {
        "scikit_learn": sklearn.__version__,
        "seed": SEED,
        "cv_f1_mean": round(cv_f1.mean(), 3),
        "test": test_scores,
    }
    Path("metrics.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    print("Saved churn_model.joblib and metrics.json")


if __name__ == "__main__":
    main()
