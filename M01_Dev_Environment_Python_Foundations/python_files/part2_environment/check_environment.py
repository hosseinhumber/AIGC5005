"""Report which Python environment is running this script.

Run it from a terminal with your conda environment activated:

    python check_environment.py
"""
import os
import platform
import sys
from pathlib import Path


def describe_environment():
    prefix = Path(sys.prefix)
    is_conda = (prefix / "conda-meta").is_dir()      # every conda environment has a conda-meta folder
    name = os.environ.get("CONDA_DEFAULT_ENV") or (prefix.name if is_conda else None)

    print("Python version      :", platform.python_version())
    print("Interpreter         :", sys.executable)
    print("Environment folder  :", prefix)
    print("Conda environment?  :", is_conda)

    if not is_conda:
        print("-> Not a conda environment. Activate yours:  conda activate module01-tool")
    elif name == "base":
        print("-> You are in base. Create a project environment instead:")
        print("   conda create -n module01-tool python=3.11")
    else:
        print(f"-> Good: working in the '{name}' environment.")


if __name__ == "__main__":
    describe_environment()
