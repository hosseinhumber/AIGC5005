"""Part 5: reading and writing text files, and paths with pathlib.

Run:  python files_and_paths.py     (writes into an `output` folder next to this file)
"""
from pathlib import Path

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

# "w" creates the file, or ERASES it if it already exists.
with open(OUT / "notes.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")

# "a" appends to the end instead.
with open(OUT / "notes.txt", "a", encoding="utf-8") as f:
    f.write("appended line\n")

# The default mode "r" reads. Iterating a file gives one line at a time.
with open(OUT / "notes.txt", encoding="utf-8") as f:
    for line in f:
        print(repr(line), "->", line.strip())

# pathlib: the / operator joins paths correctly on every platform.
summary = OUT / "data" / "summary.txt"
summary.parent.mkdir(exist_ok=True)         # exist_ok avoids an error on re-runs
summary.write_text("done\n", encoding="utf-8")

print("path   :", summary)
print("exists :", summary.exists())
print("content:", summary.read_text(encoding="utf-8").strip())
