"""Tests for catalogue.models."""

import logging

import pytest

from catalogue import Book, BookUnavailableError, InvalidBookError


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("fluent python", "Fluent Python"),
        ("  clean code  ", "Clean Code"),
        ("REFACTORING", "Refactoring"),
    ],
)
def test_title_is_formatted(raw: str, expected: str) -> None:
    assert Book(raw, "Someone").title == expected


@pytest.mark.parametrize("bad_title", ["", "   "])
def test_blank_title_is_rejected(bad_title: str) -> None:
    with pytest.raises(InvalidBookError, match="needs a title"):
        Book(bad_title, "Someone")


def test_negative_copies_are_rejected() -> None:
    with pytest.raises(InvalidBookError, match="-1 copies"):
        Book("x", "Someone", copies=-1)


def test_checkout_reduces_copies(book: Book) -> None:
    book.checkout()
    assert book.copies == 1


def test_checkout_with_no_copies_raises(book: Book) -> None:
    book.checkout()
    book.checkout()
    with pytest.raises(BookUnavailableError, match="not available"):
        book.checkout()


def test_failed_checkout_leaves_copies_unchanged() -> None:
    empty = Book("x", "Someone", copies=0)
    with pytest.raises(BookUnavailableError):
        empty.checkout()
    assert empty.copies == 0


def test_checkout_is_logged(book: Book, caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO):
        book.checkout()
    assert "Checked out 'Fluent Python'; 1 left" in caplog.text


def test_round_trip_through_a_dictionary(book: Book) -> None:
    copy = Book.from_dict(book.to_dict())
    assert copy.to_dict() == book.to_dict()


def test_from_dict_reports_a_missing_field() -> None:
    with pytest.raises(InvalidBookError, match="author"):
        Book.from_dict({"title": "x"})


def test_str_shows_title_author_and_copies(book: Book) -> None:
    assert str(book) == "Fluent Python by Luciano Ramalho (2 available)"
