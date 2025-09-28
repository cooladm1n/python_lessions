# Lesson 08: Regular Expressions

Estimated time: 45-75 minutes

Learning outcomes
- Use the `re` module to find, match and replace patterns in text.
- Write and test regular expressions for common formats (emails, phones, numbers).

Acceptance criteria
- Implement `extract_emails(text: str) -> list[str]` returning plausible emails.
- Implement `extract_numbers(text: str) -> list[int]` parsing integers from text.

Worked example

```py
import re

EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

def extract_emails(text: str) -> list[str]:
	return EMAIL_RE.findall(text)

def extract_numbers(text: str) -> list[int]:
	return [int(x) for x in re.findall(r"-?\d+", text)]
```

Exercises (mandatory)
1) Implement `extract_emails` and test with sample strings.
2) Implement `extract_numbers` and test with mixed text.

Hints & testing
- Keep regexes simple and document limitations (real email validation is harder).
- Use parametrized pytest tests for multiple sample strings.


