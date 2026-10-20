# Part 3 · Pipelines and ColumnTransformer

Open `Part3_Pipelines.ipynb`.

It builds the pipeline step by step, inspects the weights beside their column names, predicts for a customer with a missing charge and an unseen payment method, and shows `set_output(transform="pandas")`. `churn_pipeline.py` is the same pipeline as a function (`build_pipeline()`, `load_split()`), reused from Part 4 onward. `customers.py` is the invented customer table.
