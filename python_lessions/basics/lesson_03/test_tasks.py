import pytest
from tasks import sum_range, is_prime, count_evens


def test_sum_range():
    assert sum_range(1) == 1
    assert sum_range(5) == 15


@pytest.mark.parametrize("n,expected", [(2, True), (3, True), (4, False), (1, False), (0, False)])
def test_is_prime(n, expected):
    assert is_prime(n) is expected


def test_count_evens():
    assert count_evens([1, 2, 3, 4, 5]) == 2
    assert count_evens([]) == 0
 
