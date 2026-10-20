"""An invented customer table for practising scikit-learn."""

import numpy as np
import pandas as pd


def make_customers(n: int = 2000, seed: int = 42) -> pd.DataFrame:
    """Return n invented customers. The churned column is 1 for a customer who left."""
    rng = np.random.default_rng(seed)
    tenure = rng.integers(1, 73, n)
    contract = rng.choice(["month-to-month", "one-year", "two-year"], n, p=[0.55, 0.25, 0.20])
    payment = rng.choice(["card", "bank transfer", "cheque"], n, p=[0.45, 0.35, 0.20])
    monthly = np.round(rng.normal(65, 20, n).clip(20, 120), 2)
    calls = rng.poisson(1.5, n)
    contract_effect = np.select([contract == "month-to-month", contract == "one-year"], [0.9, 0.0], -0.9)
    score = -1.9 - 0.03 * tenure + 0.015 * (monthly - 65) + 0.35 * calls + contract_effect
    churned = (rng.random(n) < 1 / (1 + np.exp(-score))).astype(int)
    frame = pd.DataFrame({
        "tenure_months": tenure,
        "monthly_charge": monthly,
        "support_calls": calls,
        "contract": contract,
        "payment": payment,
        "churned": churned,
    })
    frame.loc[rng.random(n) < 0.04, "monthly_charge"] = np.nan   # some charges are missing
    return frame
