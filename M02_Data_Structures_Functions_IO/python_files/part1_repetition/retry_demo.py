"""Part 1: the while loop, retrying until the entry is valid.

Run:  python retry_demo.py     (try letters, an empty entry, 150, then 72)
"""
while True:
    raw = input("Enter a mark out of 100: ")

    # isdigit() is False for "", "abc", "-5" and "7.5", so it doubles as
    # a check that int() will succeed. The range test only runs if it does,
    # because `and` short-circuits.
    if raw.isdigit() and 0 <= int(raw) <= 100:
        mark = int(raw)
        break                              # success: leave the loop

    print("  Please enter a whole number from 0 to 100.")

print(f"Accepted: {mark}")
