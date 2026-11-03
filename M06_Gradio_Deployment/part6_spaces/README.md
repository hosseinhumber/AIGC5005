# Part 6 · Publishing to Hugging Face Spaces

    python churn_model.py        # once, in this environment
    python prepare_space.py      # collects the five files into space_upload/
    python -m pytest -q

Then create a Gradio Space on huggingface.co and upload the five files from `space_upload/`: `app.py`, `predict.py`, `churn_model.joblib`, `requirements.txt` and `README.md`.

| File | What it is |
|---|---|
| `prepare_space.py` | Copies the files a Space needs, writes a short `requirements.txt` with exact versions (Gradio left out), and stops if the model was saved by a different scikit-learn version |
| `space_README_template.md` | The settings block and an honest description. Edit the numbers if yours differ. `sdk_version` is the Gradio version installed here |
| `test_prepare_space.py` | Two tests for the requirements text |
| `app.py`, `predict.py` | The finished app and inference module |

`space_upload/` is generated, so it is ignored by Git. Check that `sdk_version` in the README matches `pip show gradio` before you upload.
