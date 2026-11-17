"""Run both frameworks on the same data and print one comparison table."""

import numpy as np
import torch
from torch import nn

from churn_data import make_splits
from churn_net import ChurnNet
from keras_net import build_keras_net
from train_keras import train as train_keras
from train_torch import train as train_torch

SEEDS = (42, 1, 2)


def copy_torch_into_keras(torch_net: ChurnNet, keras_net) -> None:
    """Keras keeps a kernel as (in, out), PyTorch as (out, in), so transpose."""
    linears = [m for m in torch_net.layers if isinstance(m, nn.Linear)]
    for linear, dense in zip(linears, keras_net.layers, strict=True):
        dense.set_weights(
            [linear.weight.detach().numpy().T, linear.bias.detach().numpy()]
        )


def same_weights_gap() -> float:
    """Largest difference between the two frameworks' predictions, same weights."""
    splits = make_splits(42)
    torch.manual_seed(0)
    torch_net = ChurnNet(splits.n_features).eval()
    keras_net = build_keras_net(splits.n_features)
    copy_torch_into_keras(torch_net, keras_net)
    with torch.no_grad():
        a = torch_net(splits.val.x).numpy()
    b = keras_net.predict(splits.val.x.numpy(), verbose=0).ravel()
    return float(np.abs(a - b).max())


def main() -> None:
    print(f"Same weights, largest prediction gap: {same_weights_gap():.1e}")
    row = "{:>4}  {:<9}  {:>10}  {:>7}  {:>7}"
    print(row.format("seed", "framework", "best epoch", "test F1", "seconds"))
    for seed in SEEDS:
        for run in (train_torch(seed, path=None), train_keras(seed, path=None)):
            print(
                row.format(
                    seed,
                    run["framework"],
                    run["best_epoch"],
                    f"{run['test_f1']:.3f}",
                    f"{run['seconds']:.1f}",
                )
            )


if __name__ == "__main__":
    main()
