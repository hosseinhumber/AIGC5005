"""Tests for catalogue.recommend."""

from catalogue import Book
from catalogue.recommend import pick_books


def titles(chosen: list[Book]) -> list[str]:
    return [book.title for book in chosen]


def test_same_seed_gives_the_same_books(books: list[Book]) -> None:
    assert titles(pick_books(books, 3, seed=1)) == titles(pick_books(books, 3, seed=1))


def test_different_seeds_can_give_different_books(books: list[Book]) -> None:
    results = {tuple(titles(pick_books(books, 3, seed=s))) for s in range(10)}
    assert len(results) > 1


def test_a_known_seed_gives_a_known_answer(books: list[Book]) -> None:
    assert titles(pick_books(books, 2, seed=42)) == ["Foxtrot", "Alpha"]


def test_asking_for_more_than_exist_returns_all(books: list[Book]) -> None:
    assert len(pick_books(books, 99, seed=1)) == len(books)


def test_the_original_list_is_not_changed(books: list[Book]) -> None:
    before = titles(books)
    pick_books(books, 3, seed=5)
    assert titles(books) == before
