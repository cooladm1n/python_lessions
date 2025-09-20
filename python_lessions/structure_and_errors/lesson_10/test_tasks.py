import pytest
from tasks import parse_args


def test_parse_args_valid():
    ns = parse_args(["--host","0.0.0.0","--port","8080","--debug"])
    assert ns.host == "0.0.0.0"
    assert ns.port == 8080
    assert ns.debug is True


def test_parse_args_invalid_port():
    with pytest.raises(SystemExit):
        parse_args(["--port","0"])


