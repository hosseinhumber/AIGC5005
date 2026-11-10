"""Train ChurnNet with a hand-written loop and save what inference needs."""

import json

import joblib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import torch  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.metrics import f1_score, precision_score, recall_score  # noqa: E402
from torch import nn  # noqa: E402

from churn_data import make_loaders, make_splits  # noqa: E402
from churn_net import ChurnNet  # noqa: E402

EPOCHS = 80
LEARNING_RATE = 3e-3
SEED = 42


def run_epoch(model, loader, loss_fn, optimizer=None):
    """One pass over a loader. Trains if given an optimizer, else only measures."""
    training = optimizer is not None
    model.train(training)
    total, count = 0.0, 0
    scores, labels = [], []
    with torch.set_grad_enabled(training):
        for x, y in loader:
            logits = model(x)
            loss = loss_fn(logits, y)
            if training:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            total += loss.item() * len(y)
            count += len(y)
            scores.append(logits.detach())
            labels.append(y)
    return total / count, torch.cat(scores), torch.cat(labels)


def metrics(logits, labels, threshold=0.5):
    predicted = (torch.sigmoid(logits) >= threshold).int().numpy()
    truth = labels.int().numpy()
    return {
        "precision": precision_score(truth, predicted, zero_division=0),
        "recall": recall_score(truth, predicted, zero_division=0),
        "f1": f1_score(truth, predicted, zero_division=0),
    }


def main() -> None:
    torch.manual_seed(SEED)
    splits = make_splits(SEED)
    train_loader, val_loader, test_loader = make_loaders(splits, seed=SEED)

    positives = splits.train.y.sum().item()
    pos_weight = torch.tensor((len(splits.train) - positives) / positives)
    loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    model = ChurnNet(splits.n_features)
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    history = []
    best_loss, best_state, best_epoch = float("inf"), None, 0
    for epoch in range(1, EPOCHS + 1):
        train_loss, _, _ = run_epoch(model, train_loader, loss_fn, optimizer)
        val_loss, val_logits, val_labels = run_epoch(model, val_loader, loss_fn)
        val = metrics(val_logits, val_labels)
        history.append(
            {
                "epoch": epoch,
                "train_loss": train_loss,
                "val_loss": val_loss,
                "val_f1": val["f1"],
            }
        )
        if val_loss < best_loss:
            best_loss, best_epoch = val_loss, epoch
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
        if epoch == 1 or epoch % 10 == 0:
            print(
                f"epoch {epoch:3d}  train loss {train_loss:.4f}  "
                f"val loss {val_loss:.4f}  val F1 {val['f1']:.3f}"
            )

    model.load_state_dict(best_state)
    _, test_logits, test_labels = run_epoch(model, test_loader, loss_fn)
    test = metrics(test_logits, test_labels)
    print(f"Best epoch by validation loss: {best_epoch}")
    print("Test set, used once:", {k: round(v, 3) for k, v in test.items()})

    # The Module 05 style baseline, on exactly the same rows
    baseline = LogisticRegression(class_weight="balanced", max_iter=1000)
    baseline.fit(splits.train.x.numpy(), splits.train.y.numpy())
    base_pred = baseline.predict(splits.test.x.numpy())
    print(
        "Logistic regression baseline F1:",
        round(f1_score(splits.test.y.numpy(), base_pred), 3),
    )

    frame = pd.DataFrame(history)
    frame.to_csv("history.csv", index=False)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(frame["epoch"], frame["train_loss"], label="train loss")
    ax.plot(frame["epoch"], frame["val_loss"], label="validation loss")
    ax.axvline(
        best_epoch, color="grey", linestyle="--", label=f"best epoch ({best_epoch})"
    )
    ax.set_xlabel("epoch")
    ax.set_ylabel("loss")
    ax.legend()
    fig.tight_layout()
    fig.savefig("learning_curves.png", dpi=150)

    torch.save(
        {"state_dict": best_state, "n_features": splits.n_features}, "churn_net.pt"
    )
    joblib.dump(splits.preprocessor, "preprocessor.joblib")
    with open("metrics.json", "w") as f:
        json.dump(
            {"best_epoch": best_epoch, "test": test, "torch": torch.__version__},
            f,
            indent=2,
        )
    print(
        "Saved churn_net.pt, preprocessor.joblib, history.csv, "
        "learning_curves.png, metrics.json"
    )


if __name__ == "__main__":
    main()
