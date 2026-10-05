"""The 'before' script from the worked example: everything in one flat file.

Run:  python catalogue_script.py

Problems to notice: the data is a dictionary with no fixed shape (a typo in a key fails silently),
there is no reusable class, and nothing records which packages the script needs.
"""
import requests   # noqa: F401  (imported but unused here: it stands in for a real third-party dependency)

books = []


def add_book(title, author):
    books.append({"title": title.strip().title(), "author": author, "copies": 1})


def checkout(title):
    for b in books:
        if b["title"] == title and b["copies"] > 0:
            b["copies"] -= 1
            return
    raise ValueError(f"'{title}' is not available.")


add_book("fluent python", "Luciano Ramalho")
checkout("Fluent Python")
print(books)
