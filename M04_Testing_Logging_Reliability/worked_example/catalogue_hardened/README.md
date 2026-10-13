# catalogue_hardened

The Module 03 catalogue package after the changes in Module 04: a test suite, exceptions that fail usefully, logging, type hints, formatting and linting, and settings, a seed and a run record for reproducibility.

## Set up (once)

    conda env create -f environment.yml    # builds the "module04-quality" environment (Python 3.11 + pip)
    conda activate module04-quality
    pip install -r requirements.txt        # pinned pytest, mypy, ruff and ipykernel
    pip install -e .                       # makes the `catalogue` package importable from anywhere

## Run

Run from the project root, so the relative paths in the settings file work.

    python -m catalogue.main
    python -m catalogue.main --config config/catalogue.toml

The program prints three books. The same seed gives the same three every time. Each run also writes `data/processed/run_info.json`, which records the settings and the tool versions it ran with.

## Check (run all four before every commit)

    python -m ruff format .
    python -m ruff check .
    python -m mypy
    python -m pytest

## Layout

    src/catalogue/    the package
        errors.py             the exception family, all inheriting from CatalogueError
        models.py             Book, with validation and logging
        store.py              reading and writing the catalogue file
        recommend.py          choosing books at random, repeatably
        config.py             reading settings from a TOML file
        reproducibility.py    recording the environment of a run
        logging_setup.py      configuring logging, called once by main
        main.py               the entry point
    tests/            the pytest suite; conftest.py holds the shared fixtures
    config/           settings, kept out of the code
    data/             the catalogue, and the generated run record
