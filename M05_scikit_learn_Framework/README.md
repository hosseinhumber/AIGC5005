# AIGC 5005 · Module 05 · Code

Open this folder in VS Code (File > Open Folder). Everything for Module 05 is here.

## Setup (once)

    conda create -n module05-sklearn python=3.11 ipykernel
    conda activate module05-sklearn
    pip install -r requirements.txt

`requirements.txt` pins `scikit-learn`, `pandas`, `matplotlib` (for one chart in Part 5), `pytest` (worked example) and `ipykernel` (needed to run the notebooks). The numbers in the learning module were produced with these versions.

## What is here

Each part is a folder with one notebook and the small modules it uses. The notebooks are for exploring: you see arrays, tables, a confusion matrix and the pipeline drawn out right under the code that made them. The modules are what you reuse and test: `customers.py` (the invented customer table), `churn_pipeline.py` (the pipeline as a function) and, in the worked example, `churn_model.py` with its pytest tests.

Open a notebook in VS Code and choose the `module05-sklearn` kernel. Every folder is self-contained, so a notebook always finds its modules beside it. The notebooks are saved with their outputs, so you can read them before you run them, and your numbers should match.

| Module part | Folder | Notebook | Modules |
|---|---|---|---|
| Part 1: the estimator API | `part1_estimator_api/` | `Part1_Estimator_API.ipynb` | `customers.py` |
| Part 2: splitting and leakage | `part2_splitting_leakage/` | `Part2_Splitting_Leakage.ipynb` | `customers.py` |
| Part 3: pipelines and ColumnTransformer | `part3_pipelines/` | `Part3_Pipelines.ipynb` | `customers.py`, `churn_pipeline.py` |
| Part 4: cross-validation | `part4_cross_validation/` | `Part4_Cross_Validation.ipynb` | `customers.py`, `churn_pipeline.py` |
| Part 5: metrics beyond accuracy | `part5_metrics/` | `Part5_Metrics.ipynb` | `customers.py`, `churn_pipeline.py` |
| Part 6: imbalance, tuning, saving | `part6_imbalance_tuning_saving/` | `Part6_Imbalance_Tuning_Saving.ipynb` | `customers.py`, `churn_pipeline.py` |
| Worked example | `worked_example/` | `M05_Worked_Example_Churn_Model.ipynb` | `customers.py`, `churn_model.py`, `test_churn_model.py` |

In the worked example, run the script and the tests from a terminal too:

    python churn_model.py
    python -m pytest -v

Every random choice uses a seed. Some cells print warnings from your library versions. They do not change the results.

Generated files (`churn_model.joblib`, `metrics.json`, `sklearn_version.txt`) are ignored by Git through `.gitignore`.
Never load a `.joblib` file from a source you do not trust, because loading one can run code.
