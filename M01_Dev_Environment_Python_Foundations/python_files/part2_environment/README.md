# Part 2: your environment

An example of the two files the module asks you to write for your own project.

    conda env create -f environment.yml    # builds the environment named in the file
    conda activate module01-tool
    pip install -r requirements.txt        # pinned pip packages
    python check_environment.py            # confirm which Python you are using

`ipykernel` is listed so VS Code and Jupyter can run notebooks in this environment; your code never imports it.
