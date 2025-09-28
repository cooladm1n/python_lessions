# Lesson 09: Working with Files and Directories

Estimated time: 45-75 minutes

Learning outcomes
- Use `pathlib` for cross-platform path operations.
- Walk directories, match patterns, copy files and handle filesystem errors.

Acceptance criteria
- Implement `find_files(directory: str, pattern: str) -> list[str]` using `rglob`.
- Implement `copy_file(src: str, dst: str)` ensuring parent directories exist.

Worked example

```py
from pathlib import Path

def find_files(directory: str, pattern: str) -> list[str]:
	return [str(p) for p in Path(directory).rglob(pattern)]

def copy_file(src: str, dst: str) -> None:
	dstp = Path(dst)
	dstp.parent.mkdir(parents=True, exist_ok=True)
	dstp.write_bytes(Path(src).read_bytes())
```

Exercises (mandatory)
1) Implement `find_files` and test with tmp directories.
2) Implement `copy_file` and validate that destination exists and content matches.

Hints & testing
- Use `tmp_path` fixture in pytest for temporary directories.
- Handle permission errors gracefully in examples.


