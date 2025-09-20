import pytest
from tasks import safe_div, parse_int, deposit, NegativeAmountError


def test_safe_div():
    assert safe_div(10, 2) == 5
    assert safe_div(1, 0, default=None) is None


def test_parse_int():
    assert parse_int("42") == 42
    with pytest.raises(ValueError):
        parse_int("x")


def test_deposit():
    assert deposit(100, 50) == 150
    with pytest.raises(NegativeAmountError):
        deposit(100, -5)
