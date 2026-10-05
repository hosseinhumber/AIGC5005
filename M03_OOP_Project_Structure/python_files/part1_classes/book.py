"""Part 1: a class, its instances, and their methods.

Run:  python book.py
"""


class Book:
    """A single book in the catalogue."""

    def __init__(self, title, author, copies=1):
        # __init__ runs automatically when you call Book(...).
        # Each assignment below creates an INSTANCE attribute that belongs to this one object.
        self.title = title
        self.author = author
        self.copies = copies

    def checkout(self):
        """Lend one copy, or raise ValueError if none are left."""
        if self.copies <= 0:
            raise ValueError(f"No copies of '{self.title}' available.")
        self.copies -= 1

    def __str__(self):
        # Python calls this automatically for print(book) and str(book).
        return f"{self.title} by {self.author} ({self.copies} available)"


if __name__ == "__main__":
    # This block only runs when you execute the file directly, not when it is imported.
    b1 = Book("Fluent Python", "Luciano Ramalho", copies=2)
    b2 = Book("Clean Code", "Robert Martin", copies=1)

    print(b1)
    print(b2)

    b1.checkout()
    print(b1)

    b2.checkout()
    try:
        b2.checkout()               # no copies left, so this raises ValueError
    except ValueError as error:
        print(f"Caught: {error}")

    # Each instance keeps its own attributes independently.
    print(b1.copies, b2.copies)     # 1 0
