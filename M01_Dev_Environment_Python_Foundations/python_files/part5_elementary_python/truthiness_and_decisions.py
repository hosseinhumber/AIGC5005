"""Part 5: truthiness, chained comparisons and if / elif / else.

Run:  python truthiness_and_decisions.py
"""
age = 30
print(18 <= age < 65)                      # chained comparison

for value in ["", "0", 0, [], [0], None]:
    print(f"{value!r:>5} -> {bool(value)}")


def status(temperature):
    if temperature < 0:
        return "freezing"
    elif temperature < 18:
        return "cold"
    elif temperature < 26:
        return "comfortable"
    else:
        return "hot"


for t in (-5, 0, 10, 18, 25, 30):
    print(f"{t:>3} degrees is {status(t)}")
