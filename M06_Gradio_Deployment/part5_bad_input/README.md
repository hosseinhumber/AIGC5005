# Part 5 · Handling bad input at inference time

    python churn_model.py      # once
    python -m pytest -q        # seven tests, including the bad-input cases
    python app.py              # try a tenure of -5

| File | What it is |
|---|---|
| `Part5_Bad_Input.ipynb` | Shows the quiet failure (a capital letter scores as no contract), then each check rejecting or accepting its input |
| `predict.py` | Adds `check_inputs`, which raises `ValueError` with a plain message |
| `app.py` | The Blocks page, now turning a `ValueError` into a `gr.Error` and warning about an empty charge with `gr.Warning` |
| `test_predict.py` | Seven tests: valid range, a high-risk customer, a missing charge, bad tenure (parametrized) and an unknown contract |
