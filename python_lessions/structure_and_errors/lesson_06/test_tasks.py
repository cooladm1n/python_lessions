import pytest
from tasks import parse_json, get_required, get_int_in_range


def test_parse_json():
    assert parse_json('{"a":1}') == {"a": 1}
    with pytest.raises(ValueError):
        parse_json('{bad}')


def test_get_required():
    data = {"name": "app", "port": 8080}
    assert get_required(data, "name", str) == "app"
    with pytest.raises(KeyError):
        get_required(data, "host", str)
    with pytest.raises(TypeError):
        get_required(data, "port", str)


def test_get_int_in_range():
    data = {"port": 80}
    assert get_int_in_range(data, "port", 1, 65535) == 80
    with pytest.raises(ValueError):
        get_int_in_range({}, "port", 1, 10)
    with pytest.raises(ValueError):
        get_int_in_range({"port": 0}, "port", 1, 10)


