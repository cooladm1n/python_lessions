import math
import pytest
from tasks import greeting, rectangle_area, celsius_to_fahrenheit


def test_greeting():
    assert greeting("Anna", 30) == "Hello, Anna! You are 30 years old."
    assert greeting("Alice", 20) == "Hello, Alice! You are 20 years old."


def test_rectangle_area():
    assert rectangle_area(7, 3) == pytest.approx(21.0)
    assert rectangle_area(0, 10) == pytest.approx(0.0)


def test_rectangle_area_negative():
    import pytest

    with pytest.raises(ValueError):
        rectangle_area(-1, 2)


def test_celsius_to_fahrenheit():
    assert math.isclose(celsius_to_fahrenheit(0), 32.0)
    assert math.isclose(celsius_to_fahrenheit(100), 212.0)
