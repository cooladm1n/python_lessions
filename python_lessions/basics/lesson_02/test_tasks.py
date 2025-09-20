import pytest
from tasks import sign, is_leap_year, grade


def test_sign():
    assert sign(10) == "positive"
    assert sign(-5) == "negative"
    assert sign(0) == "zero"


def test_is_leap_year():
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False


def test_grade():
    assert grade(95) == "A"
    assert grade(85) == "B"
    assert grade(72) == "C"
    assert grade(60) == "D"
    assert grade(10) == "F"
    with pytest.raises(ValueError):
        grade(-1)
    with pytest.raises(ValueError):
        grade(101)
