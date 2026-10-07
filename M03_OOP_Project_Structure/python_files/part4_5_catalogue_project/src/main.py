"""Entry point. Run it from anywhere, inside the activated environment, after: pip install -e .

    python -m catalogue.main
"""
from catalogue import Book


def main():
    b = Book("fluent python", "Luciano Ramalho")
    b.checkout()
    print(b.title, b.copies)   # Fluent Python 0


if __name__ == "__main__":
    main()
