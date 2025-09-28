# Lesson 06: Strings and File I/O (with Context Managers)

Estimated time: 60-90 minutes

Learning outcomes
- Manipulate strings with common methods and format output using f-strings.
- Read and write files safely with `with` and use `pathlib` for paths.
- Handle encodings and newline differences in a cross-platform way.

Acceptance criteria
- Implement `count_lines_words_chars(path)` returning a tuple (lines, words, chars).
- Implement `replace_in_file(src, dst, old, new)` which writes replaced content to dst.

Worked example

```py
from pathlib import Path

def read_text(path: str) -> str:
	return Path(path).read_text(encoding="utf-8")

def write_text(path: str, content: str) -> None:
	Path(path).write_text(content, encoding="utf-8")

def count_lines_words_chars(path: str):
	text = read_text(path)
	lines = text.splitlines()
	words = text.split()
	return len(lines), len(words), len(text)
```

Exercises (mandatory)
1) Implement `count_lines_words_chars` and test with known sample files.
2) Implement `replace_in_file` and verify output file contents in a test using `tmp_path` fixture.

Hints & testing
- Use pytest `tmp_path` fixture to create temporary files for tests.
- Remember to specify encoding to avoid cross-platform issues.
