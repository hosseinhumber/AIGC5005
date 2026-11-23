"""Movie review sentences from the Hub, and small balanced samples of them."""

from datasets import DatasetDict, load_dataset

DATASET = "cornell-movie-review-data/rotten_tomatoes"
LABELS = ["negative", "positive"]


def load_reviews() -> DatasetDict:
    """The train, validation and test splits, with columns text and label."""
    return load_dataset(DATASET)


def small_sample(split, n: int, seed: int = 42) -> tuple[list[str], list[int]]:
    """A random sample of n rows with both labels in equal numbers."""
    picked = split.train_test_split(
        train_size=n, seed=seed, stratify_by_column="label"
    )["train"]
    return list(picked["text"]), list(picked["label"])


def as_lists(split) -> tuple[list[str], list[int]]:
    return list(split["text"]), list(split["label"])
