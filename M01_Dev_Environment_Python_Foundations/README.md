# AIGC 5005 · Module 01 · Code

Open this folder in VS Code (File > Open Folder). Everything for Module 01 is here.

## Setup (once)

    conda create -n module01-tool python=3.11 ipykernel
    conda activate module01-tool

In VS Code, pick the `module01-tool` interpreter (Ctrl+Shift+P > "Python: Select Interpreter") and use it as the notebook kernel.

The Part 4 notebook imports `ipykernel`, which the setup above installs. Nothing else needs installing: Module 01 uses only the Python standard library. (The Part 3 notebook runs the `git` command, so Git must be installed.)

## Folder map

| Module part | Notebook (`notebooks/`) | Python files (`python_files/`) |
|---|---|---|
| Part 2: your Python environment | `M01_Part2_Environment_Check.ipynb` | `part2_environment/` |
| Part 3: Git and GitHub | `M01_Part3_Git_Four_Places.ipynb` | `part3_project_template/` |
| Part 4: editor and notebook workflow | `M01_Part4_Notebook_Workflow.ipynb` | |
| Part 5: elementary Python | `M01_Part5_Elementary_Python.ipynb` | `part5_elementary_python/` |
| Worked example: Temperature Advisor | `M01_Worked_Example_Temperature_Advisor.ipynb` | `worked_example/` |

## How to run the Python files

Open a terminal in the folder shown, with `module01-tool` active, then run the file named in the table.

| Folder | Command |
|---|---|
| `python_files/part2_environment/` | `python check_environment.py` |
| `python_files/part3_project_template/` | no program: a model repository layout (see `NOTES.md`) |
| `python_files/part5_elementary_python/` | `python variables_and_numbers.py`, `python rounding_and_conversion.py`, `python truthiness_and_decisions.py`, `python read_input.py` |
| `python_files/worked_example/` | `python app.py` |

Several notebooks create a scratch folder (`scratch_part2`, `scratch_part3`) and delete it in their last cell. If a notebook stops early, delete the scratch folder by hand.
