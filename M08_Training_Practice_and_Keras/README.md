# AIGC 5005 · Module 08 · Code

Open this folder in VS Code (File > Open Folder). Everything for Module 08 is here.

## Setup (once)

    conda create -n aigc-5005-module08-keras python=3.12
    conda activate aigc-5005-module08-keras
    pip install -r requirements.txt

`requirements.txt` pins `torch`, `tensorflow` and `keras`, together with `numpy`, `pandas`, `scikit-learn`, `joblib`, `matplotlib`, `pytest` and `ipykernel` (needed to run the notebooks). The numbers in the learning module were produced with these versions on a CPU. Your numbers should match closely, and the timings will not. If you have an NVIDIA graphics card, install the matching PyTorch build from pytorch.org instead of the plain `torch` line.

TensorFlow prints several start-up messages. They are normal. The notebooks hide them with `TF_CPP_MIN_LOG_LEVEL`, and you can do the same in your own scripts, before you import Keras.

## What is here

| Module part | Folder | Notebook | Modules and scripts |
|---|---|---|---|
| Part 1: saving and restoring | `part1_checkpoints/` | `Part1_Checkpoints.ipynb` | none |
| Part 2: devices and modes | `part2_devices_and_modes/` | `Part2_Devices_and_Modes.ipynb` | none |
| Part 3: debugging training | `part3_debugging_training/` | `Part3_Debugging_Training.ipynb` | none |
| Part 4: Keras Sequential | `part4_keras_sequential/` | `Part4_Keras_Sequential.ipynb` | none |
| Part 5: the Functional API | `part5_keras_functional/` | `Part5_Keras_Functional.ipynb` | none |
| Part 6: callbacks | `part6_keras_callbacks/` | `Part6_Keras_Callbacks.ipynb` | `keras_net.py` |
| Part 7: the same model, twice | `part7_two_frameworks/` | `Part7_Two_Frameworks.ipynb` | `train_torch.py`, `train_keras.py`, `compare.py` |
| Worked example | `worked_example/` | `M08_Worked_Example_Two_Frameworks.ipynb` | the scripts above, plus tests |

Each folder is self-contained. Open the notebook and choose the `aigc-5005-module08-keras` kernel, or run the scripts from inside the folder.

## The worked example from a terminal

    cd worked_example
    python train_torch.py
    python train_keras.py
    python compare.py
    pytest

The generated files (`*.pt`, `*.keras`, `history_keras.csv`, `learning_curves_keras.png`, `*_metrics.json`) are ignored by Git.
