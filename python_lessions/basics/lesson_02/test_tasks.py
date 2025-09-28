import pytest
from tasks import classify_number, is_leap_year, grade


@pytest.mark.parametrize("n,expected", [(5, "positive"), (0, "zero"), (-3, "negative")])
def test_classify_number(n, expected):
    assert classify_number(n) == expected


@pytest.mark.parametrize("year,expected", [(2000, True), (1900, False), (2004, True), (2001, False)])
def test_is_leap_year(year, expected):
    assert is_leap_year(year) is expected


def test_grade_boundaries():
    assert grade(95) == "A"
    assert grade(85) == "B"
    assert grade(75) == "C"
    assert grade(65) == "D"
    assert grade(50) == "F"
    with pytest.raises(ValueError):
        grade(-1)
    with pytest.raises(ValueError):
        grade(101)
