# Part 2 · Loading a saved model and writing an inference function

Run `python churn_model.py` once, then open `Part2_Inference_Function.ipynb`. In a terminal:

    python -m pytest -q

| File | What it is |
|---|---|
| `Part2_Inference_Function.ipynb` | Calls the function, shows a missing value and a column-name mismatch, and runs the tests |
| `predict.py` | Loads the model once at import and exposes `predict_churn`. No Gradio |
| `test_predict.py` | Two tests that need no browser |
| `churn_model.py`, `customers.py` | Training script and data from Module 05 |
