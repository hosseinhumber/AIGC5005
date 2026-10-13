"""Small helpers that are not part of the public interface."""


def format_title(title: str) -> str:
    """Return the title with surrounding spaces removed and each word capitalized."""
    return title.strip().title()
