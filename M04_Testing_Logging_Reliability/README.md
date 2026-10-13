# AIGC 5005 · Module 04 · Code

Open this folder in VS Code (File > Open Folder). Everything for Module 04 is here.

## Setup (once)

    conda create -n module04-quality python=3.11 ipykernel
    conda activate module04-quality
    pip install -r requirements.txt

`requirements.txt` pins `pytest`, `mypy` and `ruff`, the three tools this module uses, and `ipykernel`, which the one notebook needs.

## What is here

Every part is a folder of small Python files, because the tools in this module (pytest, mypy, ruff) are run from the terminal. Open a terminal in the folder, with `module04-quality` active, and run the commands shown. Each folder has its own `README.md`.

| Module part | Folder | Commands |
|---|---|---|
| Part 1: testing with pytest | `part1_testing/` | `python -m pytest -v` |
| Part 2: exceptions and logging | `part2_exceptions_logging/` | `python exceptions_demo.py`, `python logging_demo.py` |
| Part 3: type hints and mypy | `part3_type_hints/` | `python typed_functions.py`, `python -m mypy typed_functions.py`, `python -m mypy type_errors.py` (never run `type_errors.py` itself) |
| Part 4: formatting, linting, review | `part4_linting/` | see its `README.md`; `messy.py` is untidy on purpose |
| Part 5: reproducibility | `part5_reproducibility/` | `python seeds_demo.py`, `python config_demo.py`, `python record_environment.py` |
| Worked example | `worked_example/` | see below |

## Worked example

| Item | What it is |
|---|---|
| `worked_example/before_hardening/` | The Module 03 catalogue project, where Module 03 left it |
| `worked_example/catalogue_hardened/` | The same project after the worked example: tests, errors, logging, types, settings and a seed |
| `worked_example/M04_Worked_Example_Hardening.ipynb` | A guided tour of the hardened project. It copies it to a scratch folder, runs the four checks and the program, and deletes the scratch folder in its last cell |

Run the notebook with the `module04-quality` kernel. If it stops early, delete the `scratch_worked` folder by hand.
