"""Exceptions raised by the catalogue package.

Every one of them inherits from CatalogueError, so a caller can catch
the whole family in one place, or catch a single kind when it needs to.
"""


class CatalogueError(Exception):
    """Base class for every error this package raises on purpose."""


class InvalidBookError(CatalogueError):
    """A book was described with values that cannot be right."""


class BookUnavailableError(CatalogueError):
    """A book was requested but no copies are left."""


class CatalogueFileError(CatalogueError):
    """The catalogue file is missing, unreadable or not valid JSON."""


class ConfigError(CatalogueError):
    """The settings file is missing, unreadable or incomplete."""
