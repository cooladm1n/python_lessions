import pytest
from tasks import validate_username, require_positive, parse_port


def test_validate_username():
    with pytest.raises(ValueError):
        validate_username("")
    with pytest.raises(ValueError):
        validate_username("ab")


def test_require_positive():
    with pytest.raises(ValueError):
        require_positive(0)
    with pytest.raises(ValueError):
        require_positive(-1)


def test_parse_port():
    assert parse_port("80") == 80
    with pytest.raises(ValueError):
        parse_port("0")
    with pytest.raises(ValueError):
        parse_port("70000")
    with pytest.raises(ValueError):
        parse_port("abc")


