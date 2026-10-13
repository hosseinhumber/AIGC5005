"""Part 5: recording the environment a result came from.

Run:  python record_environment.py
"""
import json
import platform
import sys
from importlib import metadata

record = {
    "python": platform.python_version(),
    "system": platform.system(),
    "interpreter": sys.executable,
    "packages": {},
}
for name in ("pytest", "mypy", "ruff"):
    try:
        record["packages"][name] = metadata.version(name)
    except metadata.PackageNotFoundError:
        record["packages"][name] = "not installed"

print(json.dumps(record, indent=2))
