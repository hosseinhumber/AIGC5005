"""Part 5: banker's rounding and converting between types.

Run:  python rounding_and_conversion.py
"""
for value in (0.5, 1.5, 2.5, 3.5):
    print(f"round({value}) = {round(value)}")      # halfway cases go to the even number

print("round(2.675, 2) =", round(2.675, 2))        # 2.67: float precision, not a rounding rule

print("int(3.9)     =", int(3.9))                  # 3, truncates
print("int(-3.9)    =", int(-3.9))                 # -3
print("int('7')     =", int("7"))
print("float('7.0') =", float("7.0"))

try:
    int("7.0")
except ValueError as error:
    print("int('7.0') -> ValueError:", error)
