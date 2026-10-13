"""The Book class."""

import logging
from typing import Any, Self

from .errors import BookUnavailableError, InvalidBookError
from .helpers import format_title

logger = logging.getLogger(__name__)


class Book:
    """A single book in the catalogue."""

    def __init__(self, title: str, author: str, copies: int = 1) -> None:
        clean_title = format_title(title)
        if not clean_title:
            raise InvalidBookError("A book needs a title.")
        if copies < 0:
            raise InvalidBookError(f"'{clean_title}' cannot have {copies} copies.")
        self.title = clean_title
        self.author = author
        self.copies = copies

    def checkout(self) -> None:
        """Lend out one copy, or raise BookUnavailableError if none are left."""
        if self.copies <= 0:
            raise BookUnavailableError(f"'{self.title}' is not available.")
        self.copies -= 1
        logger.info("Checked out '%s'; %d left", self.title, self.copies)

    def to_dict(self) -> dict[str, Any]:
        """Return the book as a plain dictionary, ready to save as JSON."""
        return {"title": self.title, "author": self.author, "copies": self.copies}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """Build a Book from a dictionary. A missing field raises InvalidBookError."""
        try:
            return cls(data["title"], data["author"], data.get("copies", 1))
        except KeyError as error:
            raise InvalidBookError(f"A book is missing the field {error}.") from error

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.copies} available)"
