"""Part 3: type hints. This file is correct; mypy reports no problems.

Run:  python typed_functions.py
Check: python -m mypy typed_functions.py
"""
from collections.abc import Sequence


def average(values: Sequence[float]) -> float:
    """Return the mean of the values."""
    return sum(values) / len(values)


def find_user(users: dict[int, str], user_id: int) -> str | None:
    """Return the user's name, or None when there is no such user."""
    return users.get(user_id)


def greeting(users: dict[int, str], user_id: int) -> str:
    name = find_user(users, user_id)
    if name is None:                 # mypy now knows name is a str below this line
        return "Hello, stranger"
    return f"Hello, {name.title()}"


print(average([70, 80, 90]))
print(greeting({1: "ada"}, 1))
print(greeting({1: "ada"}, 2))
