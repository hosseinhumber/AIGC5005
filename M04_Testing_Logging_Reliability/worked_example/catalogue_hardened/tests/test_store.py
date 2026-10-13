"""Tests for catalogue.store. They use real files, but only inside tmp_path."""

from pathlib import Path

import pytest

from catalogue import Book, CatalogueFileError
from catalogue.store import load_books, save_books


def test_load_books_reads_every_record(catalogue_file: Path) -> None:
    books = load_books(catalogue_file)
    assert [book.title for book in books] == ["Fluent Python", "Clean Code"]


def test_save_then_load_gives_the_same_books(tmp_path: Path, books: list[Book]) -> None:
    path = tmp_path / "nested" / "books.json"
    save_books(path, books)
    assert [b.to_dict() for b in load_books(path)] == [b.to_dict() for b in books]


def test_missing_file_raises_a_clear_error(tmp_path: Path) -> None:
    with pytest.raises(CatalogueFileError, match="Cannot read"):
        load_books(tmp_path / "nothing.json")


def test_invalid_json_raises_a_clear_error(tmp_path: Path) -> None:
    path = tmp_path / "broken.json"
    path.write_text("[{", encoding="utf-8")
    with pytest.raises(CatalogueFileError, match="not valid JSON"):
        load_books(path)
