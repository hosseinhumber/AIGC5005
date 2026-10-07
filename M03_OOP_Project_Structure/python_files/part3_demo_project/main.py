
"""Entry point. Run it from anywhere, inside the activated environment, after: pip install -e .

    python -m demo_pkg.main
"""
from demo_pkg import Book, Member           # names exposed by __init__.py
from demo_pkg.helpers import format_title   # an explicit import from a submodule


def main():
    b = Book(format_title("  fluent python  "))
    m = Member("Aisha")
    print(b.title, m.name)                      # Fluent Python Aisha


if __name__ == "__main__":
    main()
