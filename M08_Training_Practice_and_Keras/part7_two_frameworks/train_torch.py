"""Train ChurnNet in PyTorch and save the best checkpoint."""

import json
import time

import torch
from sklearn.metrics import f1_score
from torch import nn

from churn_data import make_loaders, make_splits
from churn_net import ChurnNet

EPOCHS = 80
LEARNING_RATE = 3e-3
BATCH_SIZE = 64


def pick_device() -> torch.device:
    """Use a GPU when there is one, and the CPU otherwise."""
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def run_epoch(model, loader, loss_fn, device, optimizer=None):
    """One pass over a loader. Trains if given an optimizer, else only measures."""
    training = optimizer is not None
    model.train(training)
    total, count = 0.0, 0
    scores = []
    with torch.set_grad_enabled(training):
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            logits = model(x)
            loss = loss_fn(logits, y)
            if training:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            total += loss.item() * len(y)
            count += len(y)
            scores.append(logits.detach().cpu())
    return total / count, torch.cat(scores).numpy()


def train(seed: int = 42, path: str | None = "churn_net_torch.pt") -> dict:
    """Train, keep the best epoch by validation loss, and score the test rows once."""
    device = pick_device()
    torch.manual_seed(seed)
    splits = make_splits(42)
    train_loader, val_loader, test_loader = make_loaders(
        splits, batch_size=BATCH_SIZE, seed=seed
    )
    positives = splits.train.y.sum().item()
    pos_weight = torch.tensor((len(splits.train) - positives) / positives)
    loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight.to(device))

    model = ChurnNet(splits.n_features).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    best = {"val_loss": float("inf"), "epoch": 0}
    started = time.perf_counter()
    for epoch in range(1, EPOCHS + 1):
        run_epoch(model, train_loader, loss_fn, device, optimizer)
        val_loss, _ = run_epoch(model, val_loader, loss_fn, device)
        if val_loss < best["val_loss"]:
            best = {
                "val_loss": val_loss,
                "epoch": epoch,
                "model": {
                    k: v.detach().cpu().clone() for k, v in model.state_dict().items()
                },
            }
    seconds = time.perf_counter() - started

    model.load_state_dict(best["model"])
    _, logits = run_epoch(model, test_loader, loss_fn, device)
    predicted = (logits >= 0).astype(int)
    result = {
        "framework": "pytorch",
        "seed": seed,
        "best_epoch": best["epoch"],
        "best_val_loss": round(best["val_loss"], 4),
        "test_f1": round(float(f1_score(splits.test.y.numpy(), predicted)), 3),
        "seconds": round(seconds, 1),
        "version": torch.__version__,
    }
    if path:
        torch.save(
            {
                "model": best["model"],
                "n_features": splits.n_features,
                "epoch": best["epoch"],
                "val_loss": best["val_loss"],
            },
            path,
        )
    return result


if __name__ == "__main__":
    outcome = train()
    print(outcome)
    with open("torch_metrics.json", "w") as f:
        json.dump(outcome, f, indent=2)
    print("Saved churn_net_torch.pt and torch_metrics.json")
