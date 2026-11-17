"""Train the same network in Keras, with the same data, split and settings."""

import json
import time

import keras
import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from sklearn.metrics import f1_score  # noqa: E402

from churn_data import make_splits  # noqa: E402
from keras_net import build_keras_net  # noqa: E402

EPOCHS = 80
LEARNING_RATE = 3e-3
BATCH_SIZE = 64


def train(seed: int = 42, path: str | None = "churn_net.keras") -> dict:
    """Train with callbacks, keep the best epoch, and score the test rows once."""
    keras.utils.set_random_seed(seed)
    splits = make_splits(42)
    x, y = splits.train.x.numpy(), splits.train.y.numpy()
    x_val, y_val = splits.val.x.numpy(), splits.val.y.numpy()

    positives = y.sum()
    pos_weight = float((len(y) - positives) / positives)
    # class_weight reweights the training loss only. Give the validation loss
    # the same weights, so "best epoch" means the same thing as in PyTorch.
    val_weight = np.where(y_val == 1, pos_weight, 1.0).astype("float32")

    model = build_keras_net(splits.n_features)
    model.compile(
        optimizer=keras.optimizers.Adam(LEARNING_RATE),
        loss=keras.losses.BinaryCrossentropy(from_logits=True),
    )
    callbacks = [
        keras.callbacks.EarlyStopping(patience=EPOCHS, restore_best_weights=True),
    ]
    if path:
        callbacks.append(
            keras.callbacks.ModelCheckpoint(
                path, monitor="val_loss", save_best_only=True
            )
        )
    started = time.perf_counter()
    history = model.fit(
        x,
        y,
        validation_data=(x_val, y_val, val_weight),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        class_weight={0: 1.0, 1: pos_weight},
        callbacks=callbacks,
        verbose=0,
    )
    seconds = time.perf_counter() - started

    val_curve = history.history["val_loss"]
    logits = model.predict(splits.test.x.numpy(), verbose=0).ravel()
    predicted = (logits >= 0).astype(int)
    result = {
        "framework": "keras",
        "seed": seed,
        "best_epoch": int(np.argmin(val_curve)) + 1,
        "best_val_loss": round(float(min(val_curve)), 4),
        "test_f1": round(float(f1_score(splits.test.y.numpy(), predicted)), 3),
        "seconds": round(seconds, 1),
        "version": keras.__version__,
    }
    result["history"] = {
        k: [float(v) for v in vals] for k, vals in history.history.items()
    }
    return result


if __name__ == "__main__":
    outcome = train()
    curves = outcome.pop("history")
    print(outcome)
    frame = pd.DataFrame(curves)
    frame.insert(0, "epoch", range(1, len(frame) + 1))
    frame.to_csv("history_keras.csv", index=False)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.plot(frame["epoch"], frame["loss"], label="train loss")
    ax.plot(frame["epoch"], frame["val_loss"], label="validation loss")
    ax.axvline(outcome["best_epoch"], color="grey", linestyle="--", label="best epoch")
    ax.set_xlabel("epoch")
    ax.set_ylabel("loss")
    ax.legend()
    fig.tight_layout()
    fig.savefig("learning_curves_keras.png", dpi=150)
    with open("keras_metrics.json", "w") as f:
        json.dump(outcome, f, indent=2)
    print("Saved churn_net.keras, history_keras.csv, learning_curves_keras.png")
