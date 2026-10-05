# catalogue_project

A small library catalogue, refactored from one flat script into an installable package.
This is the "after" version from the Module 03 worked example.

## Set up (once)

    conda env create -f environment.yml    # builds the "catalogue" conda environment (Python 3.11 + pip)
    conda activate catalogue
    pip install -r requirements.txt        # pinned pip packages
    pip install -e .                       # makes the `catalogue` package importable from anywhere

Always install into the `catalogue` environment, never into `base`. To leave it: `conda deactivate`.

## Run

    python main.py

Expected output:

    Fluent Python 0

## Test

    python -m unittest discover -s tests

## Layout

    src/catalogue/    the package (models.py, helpers.py, __init__.py)
    tests/            automated tests
    data/raw/         inputs, never edited by code
    data/processed/   generated outputs, safe to delete
    config/           settings.example.py (copy to settings.py; settings.py is git-ignored)
    environment.yml   the conda environment (name and Python version)
    requirements.txt  pinned pip packages
    pyproject.toml    tells Python's packaging tools where the package lives

Note: `requests` is pinned only to demonstrate a pinned dependency; the catalogue code does not use it yet.
