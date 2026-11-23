# Worked example

Run from this folder:

    python compare_methods.py 42                      # four approaches, test scored once
    python compare_methods.py 1 --validation-only     # another seed, test untouched
    python curves.py 42                               # the small-data comparison
    pytest                                            # 16 tests, about a minute

`compare_methods.py` writes `worked_metrics_seed<N>.json`. `curves.py` writes a CSV and a PNG.
The saved results of the runs in the learning module are in `reference_results/`.
