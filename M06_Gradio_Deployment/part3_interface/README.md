# Part 3 · Gradio Interface

    python churn_model.py      # once
    python app.py              # then open http://127.0.0.1:7860

Or, to reload the page every time you save a change:

    gradio app.py

Stop the server with Ctrl+C. This part has no notebook, because the point is a running page, and a page is started from a terminal.

| File | What it is |
|---|---|
| `app.py` | A `gr.Interface` with five input components, a `gr.Label` output and two examples |
| `predict.py` | The inference function from Part 2 |
