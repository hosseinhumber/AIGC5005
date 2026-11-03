"""Part 4: the same function on a page of our own design, with gr.Blocks."""

import gradio as gr

from predict import CONTRACTS, PAYMENTS, predict_churn


def score(tenure, charge, calls, contract, payment, cutoff):
    chance = predict_churn(tenure, charge, calls, contract, payment)
    flag = chance >= cutoff
    action = "Flag for a retention call" if flag else "No action needed"
    return {"Will leave": chance, "Will stay": 1 - chance}, action


with gr.Blocks(title="Customer churn") as demo:
    gr.Markdown("# Customer churn\nThe chance that a customer will leave.")
    with gr.Row():
        with gr.Column():
            tenure_in = gr.Number(label="Tenure (months)", value=12, precision=0)
            charge_in = gr.Number(label="Monthly charge ($, optional)", value=70)
            calls_in = gr.Slider(0, 8, step=1, value=1, label="Support calls")
            contract_in = gr.Dropdown(CONTRACTS, label="Contract")
            payment_in = gr.Dropdown(PAYMENTS, label="Payment")
            cutoff_in = gr.Slider(0.1, 0.9, step=0.05, value=0.5, label="Threshold")
            button = gr.Button("Predict", variant="primary")
        with gr.Column():
            chances_out = gr.Label(label="Prediction")
            action_out = gr.Textbox(label="Suggested action")
    inputs = [tenure_in, charge_in, calls_in, contract_in, payment_in, cutoff_in]
    button.click(score, inputs=inputs, outputs=[chances_out, action_out])

if __name__ == "__main__":
    demo.launch()
