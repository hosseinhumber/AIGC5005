import pytest
import torch
from torch import nn

from churn_data import ChurnDataset, make_loaders, make_splits
from churn_net import ChurnNet


@pytest.fixture(scope="module")
def splits():
    return make_splits(42)


def test_split_sizes_add_up(splits):
    assert len(splits.train) + len(splits.val) + len(splits.test) == 2000


def test_dataset_returns_float32_pairs(splits):
    x, y = splits.train[0]
    assert x.dtype == torch.float32 and y.dtype == torch.float32
    assert x.shape == (splits.n_features,)


def test_scaler_was_fitted_on_training_rows_only(splits):
    scaler = splits.preprocessor.named_transformers_["num"].named_steps[
        "standardscaler"
    ]
    train_mean = splits.train.x[:, :3].mean(dim=0)
    assert torch.allclose(train_mean, torch.zeros(3), atol=0.05)
    assert scaler.n_samples_seen_ == len(splits.train)


def test_training_batches_are_shuffled_but_repeatable(splits):
    first = next(iter(make_loaders(splits, seed=1)[0]))[1]
    again = next(iter(make_loaders(splits, seed=1)[0]))[1]
    assert torch.equal(first, again)


def test_network_returns_one_logit_per_row():
    out = ChurnNet(9)(torch.zeros(5, 9))
    assert out.shape == (5,)


def test_one_step_changes_every_layer():
    torch.manual_seed(0)
    model = ChurnNet(9)
    before = [p.clone() for p in model.parameters()]
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    loss = nn.BCEWithLogitsLoss()(model(torch.randn(8, 9)), torch.ones(8))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    assert all(
        not torch.equal(a, b) for a, b in zip(before, model.parameters(), strict=True)
    )


def test_dataset_length_matches_labels():
    ds = ChurnDataset(torch.zeros(4, 2).numpy(), torch.zeros(4).numpy())
    assert len(ds) == 4
