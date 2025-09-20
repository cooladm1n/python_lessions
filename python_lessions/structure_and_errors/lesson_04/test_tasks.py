import pytest
from pathlib import Path
from tasks import read_text_safe, write_text_safe, append_line


def test_read_write_append(tmp_path: Path):
    p = tmp_path / "a" / "b.txt"
    with pytest.raises(FileNotFoundError):
        read_text_safe(p)
    write_text_safe(p, "one")
    assert read_text_safe(p) == "one"
    append_line(p, "two")
    assert read_text_safe(p).endswith("two\n")


