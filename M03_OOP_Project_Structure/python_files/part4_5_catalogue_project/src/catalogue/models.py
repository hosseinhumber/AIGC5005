from .helpers import format_title


class Book:
    """A single book in the catalogue."""

    def __init__(self, title, author, copies=1):
        self.title = format_title(title)
        self.author = author
        self.copies = copies

    def checkout(self):
        if self.copies <= 0:
            raise ValueError(f"'{self.title}' is not available.")
        self.copies -= 1
