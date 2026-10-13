"""Reading and writing the catalogue file."""

import json
import logging
from pathlib import Path

from .errors import CatalogueFileError
from .models import Book

logger = logging.getLogger(__name__)


def load_books(path: Path) -> list[Book]:
    """Read every book from a JSON file."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        raise CatalogueFileError(
            f"Cannot read the catalogue file {path}: {error.strerror}"
        ) from error
    try:
        records = json.loads(text)
    except json.JSONDecodeError as error:
        raise CatalogueFileError(
            f"{path} is not valid JSON (line {error.lineno})."
        ) from error
    books = [Book.from_dict(record) for record in records]
    logger.debug("Loaded %d books from %s", len(books), path)
    return books


def save_books(path: Path, books: list[Book]) -> None:
    """Write the books to a JSON file, creating the folder if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    records = [book.to_dict() for book in books]
    path.write_text(json.dumps(records, indent=2), encoding="utf-8")
    logger.info("Saved %d books to %s", len(books), path)
