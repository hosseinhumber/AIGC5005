"""Tests for both versions of the churn network."""

import keras
import numpy as np
import pytest
import torch
from torch import nn

from churn_data import make_splits
from churn_net import ChurnNet
from compare import copy_torch_into_keras
from keras_net import build_keras_net


@pytest.fixture(scope="module")
def splits():
    return make_splits(42)


def test_keras_net_gives_one_score_per_row(splits):
    model = build_keras_net(splits.n_features)
    scores = model.predict(splits.val.x.numpy(), verbose=0)
    assert scores.shape == (len(splits.val), 1)


@pytest.mark.parametrize("hidden", [4, 16, 64])
def test_both_networks_have_the_same_parameter_count(splits, hidden):
    torch_count = sum(
        p.numel() for p in ChurnNet(splits.n_features, hidden).parameters()
    )
    assert build_keras_net(splits.n_features, hidden).count_params() == torch_count


def test_same_weights_give_the_same_predictions(splits):
    torch.manual_seed(0)
    torch_net = ChurnNet(splits.n_features).eval()
    keras_net = build_keras_net(splits.n_features)
    copy_torch_into_keras(torch_net, keras_net)
    with torch.no_grad():
        expected = torch_net(splits.val.x).numpy()
    actual = keras_net.predict(splits.val.x.numpy(), verbose=0).ravel()
    assert np.allclose(expected, actual, atol=1e-5)


def test_keras_can_memorize_one_small_batch(splits):
    keras.utils.set_random_seed(0)
    x, y = splits.train.x.numpy()[:32], splits.train.y.numpy()[:32]
    model = build_keras_net(splits.n_features, hidden=64)
    model.compile(
        optimizer=keras.optimizers.Adam(1e-2),
        loss=keras.losses.BinaryCrossentropy(from_logits=True),
    )
    history = model.fit(x, y, epochs=300, batch_size=32, verbose=0)
    assert history.history["loss"][-1] < 0.05


def test_keras_model_survives_save_and_load(splits, tmp_path):
    model = build_keras_net(splits.n_features)
    path = tmp_path / "net.keras"
    model.save(path)
    loaded = keras.models.load_model(path)
    x = splits.val.x.numpy()
    assert np.allclose(model.predict(x, verbose=0), loaded.predict(x, verbose=0))


def test_torch_checkpoint_restores_the_same_predictions(splits, tmp_path):
    torch.manual_seed(0)
    model = ChurnNet(splits.n_features).eval()
    path = tmp_path / "net.pt"
    torch.save({"model": model.state_dict(), "n_features": splits.n_features}, path)
    checkpoint = torch.load(path, weights_only=True)
    restored = ChurnNet(checkpoint["n_features"]).eval()
    restored.load_state_dict(checkpoint["model"])
    assert torch.equal(model(splits.val.x), restored(splits.val.x))


def test_eval_mode_makes_dropout_repeatable(splits):
    torch.manual_seed(0)
    net = nn.Sequential(
        nn.Linear(splits.n_features, 8), nn.Dropout(0.5), nn.Linear(8, 1)
    )
    x = splits.val.x[:10]
    net.train()
    assert not torch.equal(net(x), net(x))
    net.eval()
    assert torch.equal(net(x), net(x))
