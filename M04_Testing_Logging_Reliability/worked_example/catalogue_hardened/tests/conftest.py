"""Fixtures shared by every test file."""

import json
from pathlib import Path

import pytest

from catalogue import Book


@pytest.fixture
def book() -> Book:
    """A book with two copies."""
    return Book("fluent python", "Luciano Ramalho", copies=2)


@pytest.fixture
def books() -> list[Book]:
    """Six books, enough for a random sample to be interesting."""
    titles = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot"]
    return [Book(title, "Author", copies=1) for title in titles]


@pytest.fixture
def catalogue_file(tmp_path: Path) -> Path:
    """A small catalogue file inside pytest's temporary folder."""
    path = tmp_path / "catalogue.json"
    records = [
        {"title": "fluent python", "author": "Luciano Ramalho", "copies": 2},
        {"title": "clean code", "author": "Robert Martin", "copies": 1},
    ]
    path.write_text(json.dumps(records), encoding="utf-8")
    return path


@pytest.fixture
def settings_file(tmp_path: Path, catalogue_file: Path) -> Path:
    """A settings file that points at the small catalogue."""
    path = tmp_path / "catalogue.toml"
    path.write_text(
        f'data_file = "{catalogue_file.as_posix()}"\n'
        f'output_dir = "{(tmp_path / "out").as_posix()}"\n'
        "seed = 7\nsample_size = 2\n",
        encoding="utf-8",
    )
    return path
