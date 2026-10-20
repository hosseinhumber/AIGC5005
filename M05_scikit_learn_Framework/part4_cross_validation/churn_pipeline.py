"""The preprocessing and model pipeline used from Part 4 onward."""

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from customers import make_customers

SEED = 42
NUMERIC = ["tenure_months", "monthly_charge", "support_calls"]
CATEGORICAL = ["contract", "payment"]


def build_pipeline(class_weight=None) -> Pipeline:
    """Imputing, scaling, encoding and a logistic regression in one object."""
    preprocess = ColumnTransformer([
        ("num", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), NUMERIC),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAL),
    ])
    model = LogisticRegression(max_iter=1000, class_weight=class_weight)
    return Pipeline([("prep", preprocess), ("model", model)])


def load_split():
    """Return X, y and the stratified 75/25 split used throughout the module."""
    customers = make_customers(seed=SEED)
    X, y = customers.drop(columns="churned"), customers["churned"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=SEED
    )
    return X, y, X_train, X_test, y_train, y_test
