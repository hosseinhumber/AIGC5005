# main.py (project root, outside src/). Needs:  pip install -e .
from catalogue import Book

b = Book("fluent python", "Luciano Ramalho")
b.checkout()
print(b.title, b.copies)   # Fluent Python 0
