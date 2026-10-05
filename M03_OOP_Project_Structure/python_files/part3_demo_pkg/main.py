"""Run from this folder:  python main.py

main.py sits OUTSIDE the demo_pkg folder, so Python can import demo_pkg as a package.
"""
from demo_pkg import Book, Member           # names exposed by __init__.py
from demo_pkg.helpers import format_title   # an explicit import from a submodule

b = Book(format_title("  fluent python  "))
m = Member("Aisha")
print(b.title, m.name)                      # Fluent Python Aisha
