"""Entry point. Run it from the project root, after: pip install -e .

python -m catalogue.main
python -m catalogue.main --config config/catalogue.toml
"""

import argparse
import logging
import sys
from pathlib import Path

from .config import load_settings
from .errors import CatalogueError
from .logging_setup import configure_logging
from .recommend import pick_books
from .reproducibility import write_run_info
from .store import load_books

logger = logging.getLogger(__name__)


def main(argv: list[str] | None = None) -> int:
    """Run the program and return its exit code (0 means success)."""
    parser = argparse.ArgumentParser(description="Suggest books from the catalogue.")
    parser.add_argument("--config", type=Path, default=Path("config/catalogue.toml"))
    args = parser.parse_args(argv)

    configure_logging("INFO")  # so that even a settings problem is logged properly
    try:
        settings = load_settings(args.config)
        configure_logging(settings.log_level)
        books = load_books(settings.data_file)
        logger.info(
            "Choosing %d books with seed %d", settings.sample_size, settings.seed
        )
        for book in pick_books(books, settings.sample_size, settings.seed):
            print(book)
        write_run_info(settings.output_dir / "run_info.json", settings)
    except CatalogueError as error:
        logger.error("Stopped: %s", error)
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
