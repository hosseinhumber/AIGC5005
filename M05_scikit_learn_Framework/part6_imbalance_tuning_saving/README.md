# Part 6 · Imbalance, tuning and saving a model

Open `Part6_Imbalance_Tuning_Saving.ipynb`.

It covers `class_weight="balanced"`, five-fold means and spreads, `GridSearchCV` on a forest pipeline (under a minute), the test set used once, and saving and loading the whole pipeline with joblib. Running it creates `churn_model.joblib` and `sklearn_version.txt` here, which Git ignores. `churn_pipeline.py` and `customers.py` are shared modules.
