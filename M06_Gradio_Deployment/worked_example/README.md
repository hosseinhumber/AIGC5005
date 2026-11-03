---
title: Customer churn
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "6.31.0"
python_version: "3.11"
app_file: app.py
---

# Customer churn

Predicts the chance that a telecom customer will leave. The data is invented.

**What it is.** A logistic regression pipeline from Module 05, trained on 2,000 invented customers.

**How well it did.** On a test set used once: precision 0.28, recall 0.76, F1 0.41, ROC-AUC 0.78.

**What it is not.** An illustration. It must not be used to make real decisions about real customers.

## Run it on your computer

    python churn_model.py
    python -m pytest -q
    python app.py

## Publish it

Upload `app.py`, `predict.py`, `churn_model.joblib`, `requirements.txt` and this `README.md` to a Gradio Space. `customers.py`, `churn_model.py` and the tests stay on your computer.
