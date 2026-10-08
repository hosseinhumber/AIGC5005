"""Part 3: lists, tuples, dictionaries and sets.

Run:  python lists_tuples_dicts_sets.py
"""


# ======================================================================
# 1. Lists
# ======================================================================

scores = [72, 88, 95]
scores.append(61)                  # add to the end

print("scores       :", scores)
print("scores[0]    :", scores[0])     # first item
print("scores[-1]   :", scores[-1])    # negative indexes count from the end
print("scores[1:3]  :", scores[1:3])   # slice; stop index excluded, as with range
print("len(scores)  :", len(scores))


# ======================================================================
# `sorted()` versus `.sort()`
# ======================================================================

scores = [72, 88, 95, 61]

new_list = sorted(scores)
print("sorted() gave  :", new_list, "| original untouched:", scores)

scores.sort()
print("after .sort()  :", scores)

# The bug: assigning the result of .sort()
scores = [72, 88, 95, 61]
scores = scores.sort()
print("scores = scores.sort() leaves scores as:", scores)     # None; the list is gone


# ======================================================================
# Assignment does not copy
# ======================================================================

a = [1, 2]
b = a              # b is a second name for the SAME list
b.append(3)
print("a:", a)     # [1, 2, 3]  a changed too
print("a is b:", a is b)

c = a.copy()       # an independent copy
c.append(99)
print("a:", a, "| c:", c, "| a is c:", a is c)


# ======================================================================
# 2. Tuples
# ======================================================================

point = (43.7, -79.4)
lat, lon = point                   # unpacking
print(f"lat={lat}, lon={lon}")

# The comma makes a tuple, not the parentheses.
print(type((5)))     # int: the parentheses only group
print(type((5,)))    # tuple

# Tuples cannot be changed. The try/except keeps the notebook running.
try:
    point[0] = 0.0
except TypeError as error:
    print("TypeError ->", error)


# ======================================================================
# 3. Dictionaries
# ======================================================================

marks = {"ada": 91, "alan": 78}
marks["grace"] = 85                # add, or update if the key exists

print(marks)
print("marks['ada']            :", marks["ada"])
print("marks.get('linus')      :", marks.get("linus"))       # None, no error
print("marks.get('linus', 0)   :", marks.get("linus", 0))    # your chosen default

try:
    marks["linus"]                 # square brackets on a missing key...
except KeyError as error:
    print("marks['linus']          : KeyError", error)

# items() gives key and value together, which is nearly always what you want.
for name, mark in marks.items():
    print(f"{name:>6}: {mark}")    # :>6 right-aligns the name in 6 characters


# ======================================================================
# The counting pattern
# ======================================================================

words = ["model", "data", "model", "train", "model"]

counts = {}
for word in words:
    # get() supplies 0 the first time a word is seen, so no special case is needed.
    counts[word] = counts.get(word, 0) + 1

print(counts)


# ======================================================================
# 4. Sets
# ======================================================================

tags = {"ml", "python", "ml"}
print("tags:", tags)                        # the duplicate is gone
print("'ml' in tags:", "ml" in tags)

enrolled = {"ada", "alan", "grace"}
submitted = {"ada", "grace"}
print("not yet submitted:", enrolled - submitted)     # set difference
print("both groups      :", enrolled & submitted)     # intersection
print("either group     :", enrolled | submitted)     # union

# A classic trap: {} is an empty DICTIONARY, not an empty set.
print(type({}))       # dict
print(type(set()))    # set
