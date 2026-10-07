# Part 3 demo project

    demo_project/
        main.ipynb      a notebook that uses the package (it sits outside the package)
        demo_pkg/       the package
            __init__.py
            catalogue.py
            helpers.py

Run the correct way: open `main.ipynb` in VS Code, select your `module03` kernel, and run the cell.

Now trigger the classic mistake on purpose (run a package file directly as a script). In a terminal, from this folder:

    python demo_pkg/catalogue.py

You should see `ImportError: attempted relative import with no known parent package`.
The fix is to run it as part of the package, from this folder:

    python -m demo_pkg.catalogue
