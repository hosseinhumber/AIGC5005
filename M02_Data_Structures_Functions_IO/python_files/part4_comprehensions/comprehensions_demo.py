"""Part 4: list, dict and set comprehensions, and when not to use them.

Run:  python comprehensions_demo.py
"""


# ======================================================================
# 1. Loop versus comprehension
# ======================================================================

# The loop version: create empty, loop, append.
squares = []
for n in range(5):
    squares.append(n * n)
print("loop         :", squares)

# The comprehension version. Read it as: "n squared, for each n in range(5)".
squares = [n * n for n in range(5)]
print("comprehension:", squares)

# Add a condition at the end to filter.
evens_squared = [n * n for n in range(5) if n % 2 == 0]
print(evens_squared)      # [0, 4, 16]


# ======================================================================
# 2. Dictionary and set comprehensions
# ======================================================================

lengths = {word: len(word) for word in ["ai", "model", "pipeline"]}
print("dict:", lengths)

initials = {name[0] for name in ["ada", "alan", "grace"]}
print("set :", initials)          # duplicates collapse automatically

# A practical one: invert a dictionary, swapping keys and values.
marks = {"ada": 91, "alan": 78, "grace": 85}
by_mark = {mark: name for name, mark in marks.items()}
print(by_mark)


# ======================================================================
# 3. When NOT to use one
# ======================================================================

records = [
    {"name": "ada", "scores": [91, 88, 95]},
    {"name": "alan", "scores": [58, 62]},
    {"name": "grace", "scores": [85, 90]},
]

# Technically correct, hard to read:
result = {r["name"]: round(sum(r["scores"]) / len(r["scores"]), 1) for r in records if r["scores"] and sum(r["scores"]) / len(r["scores"]) >= 60}
print(result)

# The same logic as a plain loop. Longer, and much easier to read and debug.
result = {}
for record in records:
    scores = record["scores"]
    if not scores:
        continue                          # guard against division by zero
    average = sum(scores) / len(scores)
    if average >= 60:
        result[record["name"]] = round(average, 1)
print(result)

# Also avoid comprehensions for side effects. This works, but builds a
# useless list of None values just to print. Use a plain for loop instead.
_ = [print(name) for name in ["ada", "alan"]]      # don't do this
