from pathlib import Path
from time import sleep
from tasks import silent_remove, try_parse_int, timeout


def test_silent_remove(tmp_path: Path):
    p = tmp_path / "x.txt"
    p.write_text("hi", encoding="utf-8")
    silent_remove(p)
    assert not p.exists()
    silent_remove(p)  # no error


def test_try_parse_int():
    assert try_parse_int("42") == 42
    assert try_parse_int("x", default=0) == 0


def test_timeout_emulation(capsys):
    with timeout(0.01):
        sleep(0.02)
    out = capsys.readouterr().out
    assert "timeout" in out.lower()


