# AIGC 5005 · Module 06 · Code

Open this folder in VS Code (File > Open Folder). Everything for Module 06 is here.

## Setup (once)

    conda create -n aigc-5005-module06-app python=3.11
    conda activate aigc-5005-module06-app
    pip install -r requirements.txt

`requirements.txt` pins `gradio`, `scikit-learn`, `pandas`, `joblib`, `pytest` and `ipykernel` (needed to run the notebooks). The numbers in the learning module were produced with these versions.

## Train the model first, in every folder

Each folder is self-contained and needs a saved model in the same folder. Run this once in each folder you use:

    python churn_model.py

It writes `churn_model.joblib` and `metrics.json`. Training in your own environment matters: a model saved by one scikit-learn version may warn, or fail, when loaded by another. The notebooks do this for you if the file is missing.

## What is here

Parts that end in a page you look at are scripts you start from a terminal. Parts that are about checking and explaining have a notebook beside the modules.

| Module part | Folder | Notebook | Modules and scripts |
|---|---|---|---|
| Part 1: why deployment | `part1_why_deployment/` | `Part1_Inspect_the_Model.ipynb` | `churn_model.py`, `customers.py` |
| Part 2: inference function | `part2_inference_function/` | `Part2_Inference_Function.ipynb` | `predict.py`, `test_predict.py` |
| Part 3: Interface | `part3_interface/` | none, run the app | `app.py`, `predict.py` |
| Part 4: Blocks | `part4_blocks/` | none, run the app | `app.py`, `predict.py` |
| Part 5: bad input | `part5_bad_input/` | `Part5_Bad_Input.ipynb` | `predict.py`, `app.py`, `test_predict.py` |
| Part 6: Spaces | `part6_spaces/` | none, run the script | `prepare_space.py`, `space_README_template.md`, `test_prepare_space.py` |
| Worked example | `worked_example/` | `M06_Worked_Example_Churn_App.ipynb` | `app.py`, `predict.py`, `test_predict.py`, Space `README.md` and `requirements.txt` |

To run an app, start it from its folder with `python app.py` and open the address it prints. Stop it with Ctrl+C. Run `gradio app.py` instead to reload the page whenever you save.

The worked example folder is the one you publish: its `README.md` already begins with the Space settings block and its `requirements.txt` is the short, pinned list a Space needs. Upload `app.py`, `predict.py`, `churn_model.joblib`, `requirements.txt` and `README.md`.

Generated files (`churn_model.joblib`, `metrics.json`, `space_upload/`) are ignored by Git through `.gitignore`. Never load a `.joblib` file from a source you do not trust, because loading one can run code.
