from tasks import add, is_even, normalize_whitespace


def test_add():
    assert add(2, 2) == 4
    assert add(-1, 1) == 0


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False


def test_normalize_whitespace():
    assert normalize_whitespace(" a  b   c ") == "a b c"
