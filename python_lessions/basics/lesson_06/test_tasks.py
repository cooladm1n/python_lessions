from pathlib import Path
from tasks import count_lwc, replace_word, write_and_read


def test_count_lwc():
    text = "Hello world\nSecond line"
    assert count_lwc(text) == (2, 3, len(text))


def test_replace_word():
    text = "Python is great. Python rocks!"
    assert replace_word(text, "Python", "PYTHON") == "PYTHON is great. PYTHON rocks!"


def test_write_and_read(tmp_path: Path):
    p = tmp_path / "x.txt"
    content = "Привет, мир!"
    assert write_and_read(p, content) == content
