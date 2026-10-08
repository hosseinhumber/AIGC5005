# app.py: Temperature Advisor (Module 01 worked example)
#
# Run:  python app.py

MIN_C = -90.0    # lowest temperature ever recorded on Earth
MAX_C = 60.0     # highest

raw = input("Enter a temperature in Celsius: ")

# Validate before converting, so a bad entry does not crash the program.
try:
    celsius = float(raw)
except ValueError:
    print(f"'{raw}' is not a number. Please enter a value like 21.5")
    raise SystemExit(1)

if not MIN_C <= celsius <= MAX_C:
    print(f"{celsius} is outside the plausible range "
          f"({MIN_C} to {MAX_C}). Please check your entry.")
    raise SystemExit(1)

fahrenheit = celsius * 9 / 5 + 32

if celsius < 0:
    advice = "Freezing. Dress for winter."
elif celsius < 18:
    advice = "Cold. Bring a jacket."
elif celsius < 26:
    advice = "Comfortable."
else:
    advice = "Hot. Stay hydrated."

print(f"{celsius:.1f} C is {fahrenheit:.1f} F. {advice}")
