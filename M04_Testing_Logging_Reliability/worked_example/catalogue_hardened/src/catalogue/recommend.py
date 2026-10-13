"""Picking books at random, in a way that can be repeated."""

import random
from collections.abc import Sequence

from .models import Book


def pick_books(books: Sequence[Book], count: int, seed: int) -> list[Book]:
    """Return up to `count` books chosen at random.

    The same books, count and seed always give the same result.
    """
    generator = random.Random(seed)
    return generator.sample(list(books), k=min(count, len(books)))
