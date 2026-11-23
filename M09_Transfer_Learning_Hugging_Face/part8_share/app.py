"""A small Gradio app. Run it with: python app.py"""

import os
import sys

import gradio as gr

from share import label_scores, load_classifier

MODEL = os.environ.get("MODEL", sys.argv[1] if len(sys.argv) > 1 else "")
if not MODEL:
    raise SystemExit("Usage: python app.py <model folder or Hub model id>")
classifier = load_classifier(MODEL)


def classify(text: str) -> dict[str, float]:
    return label_scores(classifier, text)


demo = gr.Interface(
    fn=classify,
    inputs=gr.Textbox(lines=3, label="Review sentence"),
    outputs=gr.Label(num_top_classes=2, label="Prediction"),
    title="Movie review sentiment",
    examples=[["a warm, funny and beautifully acted film"], ["dull and far too long"]],
)

if __name__ == "__main__":
    demo.launch()
