# worked_example

The churn network in both frameworks, from one folder.

    python train_torch.py     # writes churn_net_torch.pt and torch_metrics.json
    python train_keras.py     # writes churn_net.keras, history_keras.csv, learning_curves_keras.png
    python compare.py         # same weights check, then three seeds in both frameworks
    pytest

`train_torch.py` picks a GPU when one exists, keeps the best epoch by validation loss and saves a checkpoint dictionary. `train_keras.py` does the same with callbacks. `test_training.py` checks that the two networks have the same size, that copying weights gives the same predictions, and that both frameworks can save and reload a model.
