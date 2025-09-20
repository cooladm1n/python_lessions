from pathlib import Path
from tasks import find_files, copy_file, get_file_size


def test_find_files(tmp_path: Path):
    (tmp_path / "test.txt").write_text("content")
    (tmp_path / "data.json").write_text("{}")
    files = find_files(tmp_path, "*.txt")
    assert len(files) == 1
    assert files[0].name == "test.txt"


def test_copy_file(tmp_path: Path):
    src = tmp_path / "source.txt"
    dst = tmp_path / "subdir" / "dest.txt"
    src.write_text("hello")
    copy_file(src, dst)
    assert dst.exists()
    assert dst.read_text() == "hello"


def test_get_file_size(tmp_path: Path):
    f = tmp_path / "test.txt"
    f.write_text("hello")
    assert get_file_size(f) == 5
    assert get_file_size(tmp_path / "missing.txt") is None


