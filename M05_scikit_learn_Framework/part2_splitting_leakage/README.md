# Part 2 · Splitting data and avoiding leakage

Open `Part2_Splitting_Leakage.ipynb`.

It shows a stratified split (`(1500, 5) (500, 5)`), how the test churn rate wanders without `stratify`, and a leakage experiment on pure noise: selecting columns before cross-validation scores 0.85, while selecting inside a pipeline scores the honest 0.47. `customers.py` is the invented customer table.
