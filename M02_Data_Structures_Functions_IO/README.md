# AIGC 5005 · Module 02 · Code

Open this folder in VS Code (File > Open Folder). Everything for Module 02 is here.

## Setup (once)

    conda create -n module02-records python=3.11 ipykernel
    conda activate module02-records
    pip install -r python_files/part5_files_json_apis/requirements.txt

In VS Code, pick the `module02-records` interpreter (Ctrl+Shift+P > "Python: Select Interpreter") and use it as the notebook kernel. Only Part 5 needs `requests`; the other parts use the standard library.

## Folder map

| Module part | Notebook (`notebooks/`) | Python files (`python_files/`) |
|---|---|---|
| Part 1: repetition | `M02_Part1_Repetition.ipynb` | `part1_repetition/` |
| Part 2: functions | `M02_Part2_Functions.ipynb` | `part2_functions/` |
| Part 3: collections | `M02_Part3_Collections.ipynb` | `part3_collections/` |
| Part 4: comprehensions | `M02_Part4_Comprehensions.ipynb` | `part4_comprehensions/` |
| Part 5: files, JSON and web APIs | `M02_Part5_Files_JSON_APIs.ipynb` | `part5_files_json_apis/` |

## How to run the Python files

Open a terminal in the folder shown, with `module02-records` active.

| Folder | Commands |
|---|---|
| `python_files/part1_repetition/` | `python loops_demo.py`, `python retry_demo.py` |
| `python_files/part2_functions/` | `python functions_demo.py` |
| `python_files/part3_collections/` | `python lists_tuples_dicts_sets.py` |
| `python_files/part4_comprehensions/` | `python comprehensions_demo.py` |
| `python_files/part5_files_json_apis/` | `python files_and_paths.py`, `python json_demo.py`, `python api_demo.py`, `python summarize_todos.py` |

The Part 5 scripts write into an `output/` folder that Git ignores. The Part 5 notebook writes into `scratch_part5` and deletes it in its last cell; if it stops early, delete that folder by hand.

The notebooks use simulated `input()` answers so that Run All never waits for you. Set `USE_REAL_INPUT = True` in the helper cell to type them yourself.
