"""Part 5: variables, dynamic typing, division and float precision.

Run:  python variables_and_numbers.py
"""
import math
from decimal import Decimal

# --- Variables are names bound to objects; the type can change -------------
count = 12
print(type(count))        # <class 'int'>
count = 12.5
print(type(count))        # <class 'float'>
count = "twelve"
print(type(count))        # <class 'str'>

# --- Division ---------------------------------------------------------------
print("7 / 2   =", 7 / 2)        # 3.5
print("7 // 2  =", 7 // 2)       # 3
print("-7 // 2 =", -7 // 2)      # -4  floors toward negative infinity
print("7 % 2   =", 7 % 2)        # 1
print("2 ** 10 =", 2 ** 10)      # 1024

# --- Float precision --------------------------------------------------------
print(0.1 + 0.2)                             # 0.30000000000000004
print(0.1 + 0.2 == 0.3)                      # False
print(abs((0.1 + 0.2) - 0.3) < 1e-9)         # True
print(math.isclose(0.1 + 0.2, 0.3))          # True
print(Decimal("0.1") + Decimal("0.2"))       # 0.3  exact, for money
