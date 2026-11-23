# AIGC 5005 · Module 09 · Code

Open this folder in VS Code (File > Open Folder). Everything for Module 09 is here.

## Setup (once)

    conda create -n aigc-5005-module09-hf python=3.12
    conda activate aigc-5005-module09-hf
    pip install -r requirements.txt

`requirements.txt` pins `torch`, `transformers`, `datasets`, `gradio` and the other libraries, together with `pytest` and `ipykernel` (needed to run the notebooks). The numbers in the learning module were produced with these versions on a CPU. Your numbers should match closely, and the timings will not. If you have an NVIDIA graphics card, install the matching PyTorch build from pytorch.org instead of the plain `torch` line.

The first time you load a model or a dataset it is downloaded from the Hugging Face Hub and kept in a cache folder on your computer, so the first run needs an internet connection and some patience. Later runs use the copy. You do not need a Hugging Face token for this module, except in Part 8 if you choose to upload a model.

## What is here

| Module part | Folder | Notebook | Modules and scripts |
|---|---|---|---|
| Part 1: pipelines | `part1_pipelines/` | `Part1_Pipelines.ipynb` | none |
| Part 2: tokenizers | `part2_tokenizers/` | `Part2_Tokenizers.ipynb` | none |
| Part 3: the datasets library | `part3_datasets/` | `Part3_Datasets.ipynb` | `review_data.py` |
| Part 4: a baseline and feature extraction | `part4_baselines_and_features/` | `Part4_Baselines_and_Features.ipynb` | `baselines.py`, `embed.py` |
| Part 5: fine-tuning with your own loop | `part5_fine_tuning/` | `Part5_Fine_Tuning.ipynb` | `finetune.py` |
| Part 6: the Trainer class | `part6_trainer/` | `Part6_Trainer.ipynb` | `trainer_version.py` |
| Part 7: how much data is enough | `part7_small_data/` | `Part7_Small_Data.ipynb` | `curves.py` |
| Part 8: save, load and share | `part8_share/` | `Part8_Share.ipynb` | `share.py`, `app.py` |
| Worked example | `worked_example/` | `M09_Worked_Example_Choosing_An_Approach.ipynb` | `compare_methods.py` and tests |

Each folder is self-contained. Open the notebook and choose the `aigc-5005-module09-hf` kernel, or run the scripts from inside the folder.

## The worked example from a terminal

    cd worked_example
    python compare_methods.py 42
    pytest

Generated files (`saved_model/`, `trainer_output/`, `worked_metrics_seed*.json`) are ignored by Git.
