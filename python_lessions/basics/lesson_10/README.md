# Lesson 10: Data Serialization

Estimated time: 60-90 minutes

Learning outcomes
- Read and write JSON and CSV formats and understand binary serialization with pickle.
- Convert Python objects into serializable formats (dicts, lists, primitives).

Acceptance criteria
- Implement `save_json(data, path)` writing UTF-8 JSON with `indent=2`.
- Implement `load_csv(path)` returning `list[dict]` using `csv.DictReader`.

Worked example

```py
import json
import csv
from pathlib import Path

def save_json(data, path: str) -> None:
	Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def load_csv(path: str) -> list[dict]:
	with open(path, newline='', encoding='utf-8') as f:
		return list(csv.DictReader(f))
```

Exercises (mandatory)
1) Implement `save_json` and `load_csv`, test with sample files.
2) Implement `serialize_data(obj)` that converts dataclasses to dicts and handles common non-serializable types.

Hints & testing
- Use `tmp_path` in pytest to create files and validate content.
- Document limitations of `pickle` and prefer JSON for interoperability.


