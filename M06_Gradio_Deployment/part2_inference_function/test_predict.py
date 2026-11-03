from predict import predict_churn


def test_probability_is_between_zero_and_one():
    assert 0 <= predict_churn(3, 95.0, 4, "month-to-month", "cheque") <= 1


def test_a_new_high_risk_customer_scores_above_half():
    assert predict_churn(3, 95.0, 4, "month-to-month", "cheque") > 0.5
