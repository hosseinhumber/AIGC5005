"""Tests for grades.py. Run them with:  python -m pytest -v"""

import pytest

from grades import average, letter


# A test is a function whose name starts with test_. A plain assert is enough.
def test_a_high_mark_is_an_a() -> None:
    assert letter(95) == "A"


# One test, many cases: every boundary is checked, and each is reported separately.
@pytest.mark.parametrize(
    ("mark", "expected"),
    [(0, "F"), (59, "F"), (60, "C"), (69, "C"), (70, "B"), (79, "B"), (80, "A"), (100, "A")],
)
def test_letter_boundaries(mark: float, expected: str) -> None:
    assert letter(mark) == expected


# An error is behaviour too: check that the right one is raised, with the right message.
@pytest.mark.parametrize("bad_mark", [-1, 100.5, 101])
def test_marks_outside_the_range_are_rejected(bad_mark: float) -> None:
    with pytest.raises(ValueError, match="from 0 to 100"):
        letter(bad_mark)


# A fixture builds something several tests need. Each test receives a fresh copy.
@pytest.fixture
def marks() -> list[float]:
    return [70, 80, 90]


def test_average_of_three_marks(marks: list[float]) -> None:
    assert average(marks) == 80.0


def test_average_is_rounded_to_one_decimal(marks: list[float]) -> None:
    marks.append(85)
    assert average(marks) == 81.2


def test_empty_list_is_rejected() -> None:
    with pytest.raises(ValueError, match="empty"):
        average([])


# Comparing floats: pytest.approx allows for tiny rounding differences.
def test_floats_need_approx() -> None:
    assert 0.1 + 0.2 == pytest.approx(0.3)
