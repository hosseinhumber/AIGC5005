"""Save a fine-tuned model and load it again through a pipeline."""

from pathlib import Path

from transformers import pipeline


def save_model(model, tokenizer, folder: str | Path) -> Path:
    """Write the weights, the configuration and the tokenizer files to a folder."""
    folder = Path(folder)
    model.save_pretrained(folder)
    tokenizer.save_pretrained(folder)
    return folder


def load_classifier(folder_or_model_id: str | Path):
    """A text-classification pipeline from a local folder or a Hub model id."""
    return pipeline("text-classification", model=str(folder_or_model_id))


def label_scores(classifier, text: str) -> dict[str, float]:
    """The score for every label, in the form Gradio's Label component accepts."""
    results = classifier(text, top_k=None)
    return {item["label"]: float(item["score"]) for item in results}
