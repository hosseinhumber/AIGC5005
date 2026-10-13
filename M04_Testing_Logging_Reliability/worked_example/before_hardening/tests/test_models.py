"""Tests for catalogue.models. Run from the project root:  python -m unittest discover -s tests"""
import unittest

from catalogue import Book


class TestBook(unittest.TestCase):
    def test_title_is_formatted(self):
        self.assertEqual(Book("  fluent python ", "A").title, "Fluent Python")

    def test_checkout_reduces_copies(self):
        book = Book("x", "A", copies=2)
        book.checkout()
        self.assertEqual(book.copies, 1)

    def test_checkout_with_no_copies_raises(self):
        book = Book("x", "A", copies=0)
        with self.assertRaises(ValueError):
            book.checkout()


if __name__ == "__main__":
    unittest.main()
