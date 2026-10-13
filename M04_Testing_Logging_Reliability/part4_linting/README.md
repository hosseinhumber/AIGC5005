# Part 4: formatting and linting with ruff

`messy.py` is deliberately untidy. Work through it with ruff:

    python -m ruff check messy.py              # list the problems
    python -m ruff check messy.py --fix        # fix the ones that are safe to fix
    python -m ruff format --diff messy.py      # preview what the formatter would change
    python -m ruff format messy.py             # apply it

Some problems need your judgment (a mutable default argument, a function name that is not lowercase). Fix those by hand, then run both commands again until they are clean.
