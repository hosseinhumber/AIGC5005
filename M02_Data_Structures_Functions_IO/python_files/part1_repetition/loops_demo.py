"""Part 1: for loops, range, enumerate, zip, continue and nested loops.

Run:  python loops_demo.py
"""


# ======================================================================
# 1. The `for` loop walks through items
# ======================================================================

for name in ["Ada", "Grace", "Alan"]:
    print(f"Hello, {name}")


# ======================================================================
# 2. Counting with `range`
# ======================================================================

# list() makes the range visible; a range on its own produces values lazily.
print("range(5)        ->", list(range(5)))          # 0 to 4, stop excluded
print("range(2, 10, 3) ->", list(range(2, 10, 3)))   # start, stop, step
print("range(5, 0, -1) ->", list(range(5, 0, -1)))   # a negative step counts down


# ======================================================================
# 3. Position and item together: `enumerate` and `zip`
# ======================================================================

names = ["Ada", "Grace", "Alan"]
scores = [91, 85, 78]

# start=1 numbers from 1, which is what humans expect in a printed list.
for position, name in enumerate(names, start=1):
    print(f"{position}. {name}")

print()

for name, score in zip(names, scores):
    print(f"{name}: {score}")


# ======================================================================
# Watch out: `zip` stops silently at the shorter sequence
# ======================================================================

names = ["Ada", "Grace", "Alan"]
scores = [91, 85]                      # one score missing

print("Silent truncation:", list(zip(names, scores)))    # Alan has vanished

# strict=True (Python 3.10+) turns the silent problem into a loud one.
# The try/except is here only so this notebook keeps running; in real code
# you would usually let the error stop the program.
try:
    list(zip(names, scores, strict=True))
except ValueError as error:
    print("With strict=True:  ValueError ->", error)


# ======================================================================
# `continue` skips to the next pass
# ======================================================================

for n in range(1, 11):
    if n % 3 == 0:
        continue                           # skip multiples of 3
    print(n, end=" ")
print()


# ======================================================================
# 5. Nested loops
# ======================================================================

for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end="\t")        # \t is a tab, keeping columns aligned
    print()                                # new line after each row


# ======================================================================
# `break` leaves only the loop it is directly inside
# ======================================================================

for row in range(3):
    for col in range(3):
        if col == 1:
            break                          # leaves the INNER loop only
        print(f"row {row}, col {col}")
    print(f"  outer loop carries on after row {row}")
