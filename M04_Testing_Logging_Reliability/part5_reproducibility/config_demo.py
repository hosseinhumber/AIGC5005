"""Part 5: reading a settings file.

Run:  python config_demo.py
"""
import tomllib
from pathlib import Path

with Path(__file__).with_name("settings.toml").open("rb") as handle:
    settings = tomllib.load(handle)       # TOML becomes ordinary dictionaries and lists

print(settings)
print("seed        :", settings["seed"])
print("log level   :", settings["logging"]["level"])
print("missing key :", settings.get("timeout", "not set, so use a default"))
