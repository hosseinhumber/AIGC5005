"""Part 2: exceptions that fail usefully.

Run:  python exceptions_demo.py
"""
import json
from pathlib import Path


class SettingsError(Exception):
    """The settings file is missing or unusable."""


def read_port(path: Path) -> int:
    """Read the port number from a JSON settings file."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as error:
        # Say what was being attempted, and keep the original error as the cause.
        raise SettingsError(f"Settings file {path} does not exist.") from error
    try:
        return int(json.loads(text)["port"])
    except (json.JSONDecodeError, KeyError, ValueError) as error:
        raise SettingsError(f"{path} must contain a JSON object with a whole-number port.") from error


# 1. A specific exception, caught where something sensible can be done about it.
try:
    read_port(Path("no_such_file.json"))
except SettingsError as error:
    print("Caught:", error)
    print("Caused by:", repr(error.__cause__))

# 2. try / except / else / finally: each block has a single job.
def parse_count(text: str) -> int:
    try:
        count = int(text)
    except ValueError:
        print(f"{text!r} is not a whole number.")
        return 0
    else:
        print(f"Parsed {count}.")      # runs only if no exception happened
        return count
    finally:
        print("Done with", repr(text))   # runs every time


parse_count("12")
parse_count("twelve")

# 3. The anti-pattern: catching everything hides real bugs.
try:
    total = 1 / 0
except Exception:
    total = 0               # the failure is silently swallowed; nothing says why
print("total is", total, "(and nobody knows a division failed)")
