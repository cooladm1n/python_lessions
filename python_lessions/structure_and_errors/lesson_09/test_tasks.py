import os
from tasks import get_env, resolve_port, bool_env


def test_get_env(monkeypatch):
    monkeypatch.delenv("X", raising=False)
    assert get_env("X", default="y") == "y"
    monkeypatch.setenv("X", "42")
    assert get_env("X") == "42"


def test_resolve_port():
    env = {"PORT": "5000"}
    cfg = {"port": 3000}
    assert resolve_port(env, cfg, 80) == 5000
    assert resolve_port({}, cfg, 80) == 3000
    assert resolve_port({}, {}, 80) == 80


def test_bool_env(monkeypatch):
    for val in ["1", "true", "yes", "on", "TRUE"]:
        monkeypatch.setenv("FLAG", val)
        assert bool_env("FLAG") is True
    for val in ["0", "false", "no", "off", "FALSE"]:
        monkeypatch.setenv("FLAG", val)
        assert bool_env("FLAG", True) is False


