"""Part 5: input() always returns a string.

Run:  python read_input.py     (type a number when asked)
"""
raw = input("Enter a temperature in Celsius: ")
print(type(raw))                 # <class 'str'> always

try:
    celsius = float(raw)
except ValueError:
    print(f"'{raw}' is not a number. Please enter a value like 21.5")
    raise SystemExit(1)

print(f"{celsius * 9 / 5 + 32:.1f} F")
