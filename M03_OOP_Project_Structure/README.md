# AIGC 5005 · Module 03 · Code

Open this folder in VS Code (File > Open Folder). Everything for Module 03 is here.

## Setup (once)

    conda create -n module03 python=3.11 ipykernel
    conda activate module03

In VS Code, pick the `module03` interpreter (Ctrl+Shift+P > "Python: Select Interpreter") and use it as the notebook kernel.

## Folder map

| Module part | Notebook (`notebooks/`) | Python files (`python_files/`) |
|---|---|---|
| Part 1: classes | `M03_Part1_Classes.ipynb` | `part1_classes/` |
| Part 2: inheritance | `M03_Part2_Inheritance.ipynb` | `part2_inheritance/` |
| Part 3: modules, packages, imports | `M03_Part3_Modules_Packages.ipynb` | `part3_demo_pkg/` |
| Parts 4 and 5: layout, dependencies | `M03_Part4_5_Layout_and_Dependencies.ipynb` | `part4_5_catalogue_project/` |
| Worked example: refactor | `M03_Worked_Example_Refactor.ipynb` | `before_refactor/` (before), `part4_5_catalogue_project/` (after) |

## How to run the Python files

Open a terminal in the folder shown, with `module03` active, then run the file named in the table.

| Folder | Command |
|---|---|
| `python_files/part1_classes/` | `python book.py` and `python class_attributes.py` |
| `python_files/part2_inheritance/` | `python members.py` |
| `python_files/part3_demo_pkg/` | `python main.py` |
| `python_files/before_refactor/` | `python catalogue_script.py` |
| `python_files/part4_5_catalogue_project/` | see its own `README.md` |

Notebooks are kept separate from the Python files on purpose: the Part 3 notebook builds its own package in a scratch folder, and a `demo_pkg` sitting next to it would change what the import demos show. Each notebook cleans up its scratch folder when it finishes.
