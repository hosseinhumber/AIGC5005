"""A network written as a class, the pattern used for every model in this course."""

import torch
from torch import nn


class TinyNet(nn.Module):
    """Three inputs, a hidden layer of four units, one output."""

    def __init__(self) -> None:
        super().__init__()
        self.hidden = nn.Linear(3, 4)
        self.activation = nn.ReLU()
        self.out = nn.Linear(4, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.out(self.activation(self.hidden(x)))
