"""Part 5: seeds make randomness repeatable.

Run:  python seeds_demo.py   (run it twice; the output of every line is identical each time)
"""
import random

names = ["Ada", "Grace", "Alan", "Katherine", "Linus", "Margaret"]

# Unseeded: different on every run, so a bug that depends on it cannot be reproduced.
print("unseeded:", random.sample(names, 3))

# Seeded: the same seed always gives the same sequence.
random.seed(42)
print("seed 42 :", random.sample(names, 3))
random.seed(42)
print("seed 42 :", random.sample(names, 3))

# Better: a private generator, so other code cannot change your sequence.
generator = random.Random(7)
print("Random(7):", generator.sample(names, 3))
print("Random(7):", random.Random(7).sample(names, 3))
