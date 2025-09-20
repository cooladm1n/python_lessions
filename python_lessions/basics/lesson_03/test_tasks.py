from tasks import sum_range, count_evens, is_prime


def test_sum_range():
    assert sum_range(1, 5) == 15
    assert sum_range(5, 5) == 5


def test_count_evens():
    assert count_evens([1, 2, 3, 4, 5, 6]) == 3
    assert count_evens([]) == 0


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(29) is True
    assert is_prime(1) is False
