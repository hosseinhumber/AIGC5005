"""Turn the invented customer table into tensors, and wrap them in a Dataset."""

from dataclasses import dataclass

import numpy as np
import torch
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from torch.utils.data import DataLoader, Dataset

from customers import make_customers

NUMERIC = ["tenure_months", "monthly_charge", "support_calls"]
CATEGORICAL = ["contract", "payment"]
TARGET = "churned"


def make_preprocessor() -> ColumnTransformer:
    """Fill gaps, scale numbers, one-hot encode categories. Fit on training rows."""
    numeric = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
    categorical = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    return ColumnTransformer(
        [("num", numeric, NUMERIC), ("cat", categorical, CATEGORICAL)]
    )


class ChurnDataset(Dataset):
    """Holds features and labels as tensors and hands out one row at a time."""

    def __init__(self, features: np.ndarray, labels: np.ndarray) -> None:
        self.x = torch.tensor(features, dtype=torch.float32)
        self.y = torch.tensor(labels, dtype=torch.float32)

    def __len__(self) -> int:
        return len(self.y)

    def __getitem__(self, index: int):
        return self.x[index], self.y[index]


@dataclass
class Splits:
    train: ChurnDataset
    val: ChurnDataset
    test: ChurnDataset
    preprocessor: ColumnTransformer

    @property
    def n_features(self) -> int:
        return self.train.x.shape[1]


def make_splits(seed: int = 42) -> Splits:
    """Split 60/20/20, fit the preprocessor on training rows, transform all three."""
    frame = make_customers(seed=seed)
    train_df, rest = train_test_split(
        frame, test_size=0.4, stratify=frame[TARGET], random_state=seed
    )
    val_df, test_df = train_test_split(
        rest, test_size=0.5, stratify=rest[TARGET], random_state=seed
    )
    prep = make_preprocessor()
    prep.fit(train_df[NUMERIC + CATEGORICAL])

    def build(df) -> ChurnDataset:
        return ChurnDataset(
            prep.transform(df[NUMERIC + CATEGORICAL]), df[TARGET].to_numpy()
        )

    return Splits(build(train_df), build(val_df), build(test_df), prep)


def make_loaders(splits: Splits, batch_size: int = 64, seed: int = 42):
    """Shuffle the training batches. Validation and test keep their order."""
    generator = torch.Generator().manual_seed(seed)
    train = DataLoader(
        splits.train, batch_size=batch_size, shuffle=True, generator=generator
    )
    val = DataLoader(splits.val, batch_size=256)
    test = DataLoader(splits.test, batch_size=256)
    return train, val, test
