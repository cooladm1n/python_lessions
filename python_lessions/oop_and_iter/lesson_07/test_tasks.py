from pathlib import Path
from tasks import Timer, FileLock, DatabaseConnection


def test_timer():
    with Timer() as t:
        import time
        time.sleep(0.01)
    assert t.duration is not None
    assert t.duration > 0


def test_file_lock(tmp_path: Path):
    file_path = tmp_path / "test.txt"
    with FileLock(file_path):
        assert file_path.with_suffix('.lock').exists()
    assert not file_path.with_suffix('.lock').exists()


def test_database_connection():
    with DatabaseConnection("sqlite:///:memory:") as db:
        assert db.connection is not None
    # Connection should be closed after context


