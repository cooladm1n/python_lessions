import pytest
from tasks import cached, retry, Singleton


def test_cached():
    call_count = 0

    @cached
    def expensive_func(x):
        nonlocal call_count
        call_count += 1
        return x * 2

    assert expensive_func(5) == 10
    assert expensive_func(5) == 10
    assert call_count == 1  # Should be cached


def test_retry():
    attempt_count = 0

    @retry(max_attempts=3)
    def flaky_func():
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise ValueError("Temporary failure")
        return "success"

    result = flaky_func()
    assert result == "success"
    assert attempt_count == 3


def test_singleton():
    class Database(metaclass=Singleton):
        def __init__(self):
            self.data = []

    db1 = Database()
    db2 = Database()
    assert db1 is db2
    db1.data.append("test")
    assert "test" in db2.data


