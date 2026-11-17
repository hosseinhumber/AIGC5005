"""A small feedforward network for the churn table."""

import torch
from torch import nn


class ChurnNet(nn.Module):
    """Two hidden layers. Returns one raw score (a logit) per customer."""

    def __init__(self, n_features: int, hidden: int = 16) -> None:
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(n_features, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.layers(x).squeeze(1)
