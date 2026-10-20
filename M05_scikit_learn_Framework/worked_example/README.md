# Worked example · A churn model from start to finish

| File | What it is |
|---|---|
| `M05_Worked_Example_Churn_Model.ipynb` | Runs the script, reads the record it wrote, uses the saved model on a new customer, and runs the tests |
| `churn_model.py` | The training script: build the pipeline, cross-validate, score the test set once, save the model and `metrics.json` |
| `test_churn_model.py` | Four pytest tests in the style of Module 04 |
| `customers.py` | The invented customer table |

From a terminal:

    python churn_model.py
    python -m pytest -v

Expect:

    Cross-validated F1 on the training data: 0.370 +/- 0.014
    Test set, used once: {'precision': 0.281, 'recall': 0.761, 'f1': 0.411, 'roc_auc': 0.781}
    Saved churn_model.joblib and metrics.json
