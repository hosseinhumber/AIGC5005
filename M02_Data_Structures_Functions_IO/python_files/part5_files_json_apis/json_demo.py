"""Part 5: JSON round trips, and why dictionary keys become strings.

Run:  python json_demo.py     (writes into an `output` folder next to this file)
"""
import json
from pathlib import Path

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

record = {"name": "Ada", "scores": [91, 88], "active": True, "mentor": None}

text = json.dumps(record, indent=2)         # Python to JSON text
print(text)                                 # True -> true, None -> null
print("round trip equal:", json.loads(text) == record)

with open(OUT / "record.json", "w", encoding="utf-8") as f:
    json.dump(record, f, indent=2)
with open(OUT / "record.json", encoding="utf-8") as f:
    print(json.load(f))

# JSON keys are always strings: integer keys do not survive a round trip.
original = {1: "a", 2: "b"}
reloaded = json.loads(json.dumps(original))
print("original keys:", list(original))
print("reloaded keys:", list(reloaded))
print("reloaded.get(1)  :", reloaded.get(1))       # None
print("reloaded.get('1'):", reloaded.get("1"))     # 'a'
