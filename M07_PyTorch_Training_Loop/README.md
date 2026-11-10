# AIGC 5005 · Module 07 · Code

Open this folder in VS Code (File > Open Folder). Everything for Module 07 is here.

## Setup (once)

    conda create -n aigc-5005-module07-torch python=3.12
    conda activate aigc-5005-module07-torch
    pip install -r requirements.txt

`requirements.txt` pins `torch`, `numpy`, `pandas`, `scikit-learn`, `joblib`, `matplotlib`, `pytest` and `ipykernel` (needed to run the notebooks). The numbers in the learning module were produced with these versions on a CPU. Your numbers should match closely. If you have an NVIDIA graphics card, install the matching build from pytorch.org instead of the plain `torch` line, and expect small differences in the last digits.

## What is here

| Module part | Folder | Notebook | Modules and scripts |
|---|---|---|---|
| Start here: what is a neural network | `part0_neural_network/` | `Part0_What_Is_a_Neural_Network.ipynb` | none |
| Part 1: the loop by hand | `part1_loop_by_hand/` | `Part1_Loop_by_Hand.ipynb` | none |
| Part 2: tensors | `part2_tensors/` | `Part2_Tensors.ipynb` | none |
| Part 3: autograd | `part3_autograd/` | `Part3_Autograd.ipynb` | none |
| Part 4: nn.Module | `part4_modules/` | `Part4_nn_Module.ipynb` | `tiny_net.py` |
| Part 5: loss and optimizers | `part5_loss_optimizers/` | `Part5_Loss_and_Optimizers.ipynb` | none |
| Part 6: Dataset and loop | `part6_dataset_and_loop/` | `Part6_Dataset_and_Loop.ipynb` | `churn_data.py`, `churn_net.py`, `customers.py`, `test_training.py` |
| Worked example | `worked_example/` | `M07_Worked_Example_Churn_Network.ipynb` | `train.py`, `predict.py`, `churn_data.py`, `churn_net.py`, tests |

Each folder is self-contained. Open the notebook and choose the `aigc-5005-module07-torch` kernel, or run the scripts from inside the folder.

## The worked example from a terminal

    cd worked_example
    python train.py
    pytest

`train.py` writes `churn_net.pt`, `preprocessor.joblib`, `history.csv`, `learning_curves.png` and `metrics.json`. `predict.py` needs the first two, so train before you run the prediction tests. These generated files are ignored by Git.
