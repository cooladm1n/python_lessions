import pytest
from tasks import greet, mean, clamp


def test_greet():
    assert greet("Ada") == "Hello, Ada."
    assert greet("Bob", excited=True) == "Hello, Bob!!!"


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        mean([])


def test_clamp():
    assert clamp(5, min_value=0, max_value=10) == 5
    assert clamp(-1, min_value=0, max_value=10) == 0
    assert clamp(99, min_value=0, max_value=10) == 10
