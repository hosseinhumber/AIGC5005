# Part 3 demo package

Run the correct way:

    python main.py

Now trigger the classic mistake on purpose (run a package file directly as a script):

    python demo_pkg/catalogue.py

You should see `ImportError: attempted relative import with no known parent package`.
The fix is to run it as part of the package, from this folder:

    python -m demo_pkg.catalogue
