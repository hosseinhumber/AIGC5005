"""Part 3: a function becomes a web page with gr.Interface."""

import gradio as gr

from predict import CONTRACTS, PAYMENTS, predict_churn


def score(tenure, charge, calls, contract, payment):
    chance = predict_churn(tenure, charge, calls, contract, payment)
    return {"Will leave": chance, "Will stay": 1 - chance}


demo = gr.Interface(
    fn=score,
    inputs=[
        gr.Number(label="Tenure (months)", value=12, precision=0),
        gr.Number(label="Monthly charge ($)", value=70),
        gr.Slider(0, 8, step=1, value=1, label="Support calls"),
        gr.Dropdown(CONTRACTS, label="Contract"),
        gr.Dropdown(PAYMENTS, label="Payment"),
    ],
    outputs=gr.Label(num_top_classes=2, label="Prediction"),
    title="Customer churn",
    examples=[
        [3, 95.0, 4, "month-to-month", "cheque"],
        [60, 40.0, 0, "two-year", "card"],
    ],
)

if __name__ == "__main__":
    demo.launch()
