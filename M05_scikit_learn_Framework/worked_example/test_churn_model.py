"""Tests for churn_model.py, in the style of Module 04. Run with:  python -m pytest -v"""

import numpy as np
import pandas as pd
import pytest

from churn_model import build_pipeline, evaluate
from customers import make_customers


@pytest.fixture(scope="module")
def sample():
    customers = make_customers(n=400, seed=7)
    return customers.drop(columns="churned"), customers["churned"]


def test_make_customers_is_repeatable():
    first = make_customers(n=50, seed=1)
    second = make_customers(n=50, seed=1)
    pd.testing.assert_frame_equal(first, second)


def test_pipeline_gives_probabilities_between_0_and_1(sample):
    X, y = sample
    probabilities = build_pipeline().fit(X, y).predict_proba(X)
    assert probabilities.shape == (400, 2)
    assert ((probabilities >= 0) & (probabilities <= 1)).all()
    assert probabilities.sum(axis=1) == pytest.approx(1.0)


def test_pipeline_handles_missing_value_and_unseen_category(sample):
    X, y = sample
    pipe = build_pipeline().fit(X, y)
    new = pd.DataFrame([{
        "tenure_months": 5, "monthly_charge": np.nan, "support_calls": 3,
        "contract": "month-to-month", "payment": "bitcoin",
    }])
    assert pipe.predict_proba(new).shape == (1, 2)


def test_evaluate_reports_four_metrics(sample):
    X, y = sample
    scores = evaluate(build_pipeline().fit(X, y), X, y)
    assert set(scores) == {"precision", "recall", "f1", "roc_auc"}
    assert all(0.0 <= value <= 1.0 for value in scores.values())
