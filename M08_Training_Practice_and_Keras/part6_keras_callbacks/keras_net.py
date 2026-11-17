"""The same small network as ChurnNet, written in Keras."""

import keras
from keras import layers


def build_keras_net(n_features: int, hidden: int = 16) -> keras.Model:
    """Two hidden layers. Returns one raw score (a logit) per customer."""
    return keras.Sequential(
        [
            keras.Input(shape=(n_features,)),
            layers.Dense(hidden, activation="relu"),
            layers.Dense(hidden, activation="relu"),
            layers.Dense(1),
        ],
        name="churn_net",
    )
