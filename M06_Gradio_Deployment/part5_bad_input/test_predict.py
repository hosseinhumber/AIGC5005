import pytest

from predict import predict_churn


def test_probability_is_between_zero_and_one():
    assert 0 <= predict_churn(3, 95.0, 4, "month-to-month", "cheque") <= 1


def test_known_customer_is_high_risk():
    assert predict_churn(3, 95.0, 4, "month-to-month", "cheque") > 0.5


def test_a_missing_charge_is_allowed():
    assert 0 <= predict_churn(3, None, 4, "month-to-month", "cheque") <= 1


@pytest.mark.parametrize("bad", [None, -1, 500])
def test_bad_tenure_is_rejected(bad):
    with pytest.raises(ValueError, match="Tenure"):
        predict_churn(bad, 95.0, 4, "month-to-month", "cheque")


def test_unknown_contract_is_rejected():
    with pytest.raises(ValueError, match="Contract must be one of"):
        predict_churn(3, 95.0, 4, "weekly", "cheque")
