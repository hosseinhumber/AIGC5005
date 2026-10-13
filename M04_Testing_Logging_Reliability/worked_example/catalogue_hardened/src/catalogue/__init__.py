"""A small library catalogue, used to practise testing, logging and reliability."""

from .errors import (
    BookUnavailableError,
    CatalogueError,
    CatalogueFileError,
    ConfigError,
    InvalidBookError,
)
from .models import Book

__all__ = [
    "Book",
    "BookUnavailableError",
    "CatalogueError",
    "CatalogueFileError",
    "ConfigError",
    "InvalidBookError",
]
