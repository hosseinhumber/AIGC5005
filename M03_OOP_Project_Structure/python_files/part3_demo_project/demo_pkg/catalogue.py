"""Core classes for the catalogue package."""
from .helpers import format_title   # relative import: only works when this file is imported AS PART OF the package


class Book:
    def __init__(self, title, copies=1):
        self.title = format_title(title)
        self.copies = copies


class Member:
    def __init__(self, name):
        self.name = name
