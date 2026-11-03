# Part 4 · Gradio Blocks

    python churn_model.py      # once
    python app.py

| File | What it is |
|---|---|
| `app.py` | A `gr.Blocks` page: a Row with two Columns, a Button and a `click` event, and a threshold slider that decides the suggested action |
| `predict.py` | The inference function from Part 2 |

Move the threshold slider and press Predict again to see the suggested action change while the probability stays the same.
