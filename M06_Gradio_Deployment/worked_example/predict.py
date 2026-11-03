"""Inference code for the churn model. No Gradio here, so it is easy to test."""

from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path(__file__).parent / "churn_model.joblib"
CONTRACTS = ["month-to-month", "one-year", "two-year"]
PAYMENTS = ["card", "cheque", "bank transfer"]

model = joblib.load(MODEL_PATH)  # runs once, when the module is first imported


def check_inputs(tenure, charge, calls, contract, payment):
    """Raise ValueError with a plain message if the customer cannot be scored."""
    if tenure is None or not 0 <= tenure <= 120:
        raise ValueError("Tenure must be a number from 0 to 120 months.")
    if charge is not None and not 0 <= charge <= 500:
        raise ValueError("Monthly charge must be from 0 to 500, or left empty.")
    if calls is None or not 0 <= calls <= 50:
        raise ValueError("Support calls must be a number from 0 to 50.")
    if contract not in CONTRACTS:
        raise ValueError(f"Contract must be one of: {', '.join(CONTRACTS)}.")
    if payment not in PAYMENTS:
        raise ValueError(f"Payment must be one of: {', '.join(PAYMENTS)}.")


def predict_churn(tenure, charge, calls, contract, payment):
    """Return the probability, from 0 to 1, that this customer will leave."""
    check_inputs(tenure, charge, calls, contract, payment)
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
