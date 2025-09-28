import pytest
from tasks import add, is_even, normalize_whitespace


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


@pytest.mark.parametrize("n,expected", [(0, True), (1, False), (2, True), (-3, False)])
def test_is_even(n, expected):
    assert is_even(n) is expected


def test_normalize_whitespace():
    assert normalize_whitespace("  a   b  c \t") == "a b c"
    assert normalize_whitespace("\nfoo\n") == "foo"
