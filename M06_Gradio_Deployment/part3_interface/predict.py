"""Inference code for the churn model. No Gradio here, so it is easy to test."""

from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path(__file__).parent / "churn_model.joblib"
CONTRACTS = ["month-to-month", "one-year", "two-year"]
PAYMENTS = ["card", "cheque", "bank transfer"]

model = joblib.load(MODEL_PATH)  # runs once, when the module is first imported


def predict_churn(tenure, charge, calls, contract, payment):
    """Return the probability, from 0 to 1, that this customer will leave."""
    row = pd.DataFrame(
        [
            {
                "tenure_months": tenure,
                "monthly_charge": charge,
                "support_calls": calls,
                "contract": contract,
                "payment": payment,
            }
        ]
    )
    return float(model.predict_proba(row)[0, 1])
