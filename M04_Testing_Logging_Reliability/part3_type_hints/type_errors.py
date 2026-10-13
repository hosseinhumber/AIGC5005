"""Part 3: five mistakes that mypy finds before the program runs.

Do NOT run this file. Check it instead:  python -m mypy type_errors.py
"""


def total_price(quantity: int, unit_price: float) -> float:
    return quantity * unit_price


# 1. Wrong argument type: a string where a number is expected.
total_price("3", 2.5)

# 2. Wrong return type: the function promises a float.
def label(value: float) -> float:
    return f"{value:.1f}"

# 3. Missing None check: the result may be None.
def find_user(users: dict[int, str], user_id: int) -> str | None:
    return users.get(user_id)

print(find_user({1: "ada"}, 1).title())

# 4. A function with no annotations at all (reported because the project sets disallow_untyped_defs).
def unchecked(x, y):
    return x + y

# 5. Misspelled attribute.
print("text".uper())
