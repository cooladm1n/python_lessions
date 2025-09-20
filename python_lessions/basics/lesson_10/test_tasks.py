from pathlib import Path
from tasks import save_json, load_csv, serialize_data


def test_save_json(tmp_path: Path):
    data = {"name": "Alice", "age": 30}
    path = tmp_path / "data.json"
    save_json(data, path)
    assert path.exists()
    content = path.read_text(encoding="utf-8")
    assert "Alice" in content


def test_load_csv(tmp_path: Path):
    csv_content = "name,age\nAlice,30\nBob,25"
    path = tmp_path / "data.csv"
    path.write_text(csv_content)
    rows = load_csv(path)
    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"


def test_serialize_data():
    from datetime import date
    obj = {"date": date(2023, 12, 25), "count": 42}
    result = serialize_data(obj)
    assert isinstance(result["date"], str)
    assert result["count"] == 42


