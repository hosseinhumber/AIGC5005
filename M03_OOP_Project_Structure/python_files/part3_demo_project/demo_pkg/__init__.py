"""Public interface of the demo_pkg package."""
# Re-export the names users should rely on, so they can write: from demo_pkg import Book
from .catalogue import Book, Member

__all__ = ["Book", "Member"]
