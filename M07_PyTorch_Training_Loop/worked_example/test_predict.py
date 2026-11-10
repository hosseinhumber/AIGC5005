from predict import predict_churn


def test_probability_is_between_zero_and_one():
    assert 0.0 <= predict_churn(2, 95.0, 5, "month-to-month", "card") <= 1.0


def test_risky_customer_scores_higher_than_loyal_one():
    risky = predict_churn(2, 95.0, 5, "month-to-month", "card")
    loyal = predict_churn(60, 40.0, 0, "two-year", "bank transfer")
    assert risky > loyal


def test_missing_charge_is_handled():
    assert 0.0 <= predict_churn(12, float("nan"), 1, "one-year", "card") <= 1.0
