"""Score one customer with the trained network, preparing it as training did."""

from pathlib import Path

import joblib
import pandas as pd
import torch

from churn_data import CATEGORICAL, NUMERIC
from churn_net import ChurnNet

HERE = Path(__file__).parent

preprocessor = joblib.load(HERE / "preprocessor.joblib")  # loaded once
checkpoint = torch.load(HERE / "churn_net.pt", weights_only=True)
model = ChurnNet(checkpoint["n_features"])
model.load_state_dict(checkpoint["state_dict"])
model.eval()  # switch off training-only behaviour


def predict_churn(tenure, charge, calls, contract, payment) -> float:
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
    )[NUMERIC + CATEGORICAL]
    features = torch.tensor(preprocessor.transform(row), dtype=torch.float32)
    with torch.no_grad():
        return float(torch.sigmoid(model(features)).item())
