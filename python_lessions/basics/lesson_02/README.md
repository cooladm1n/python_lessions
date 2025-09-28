# Lesson 02: Conditions (if/elif/else) and Boolean Logic

Estimated time: 45-60 minutes

Learning outcomes
- Read and write conditional statements using `if`, `elif`, `else`.
- Use comparison and boolean operators correctly and readably.
- Apply guard clauses and conditional expressions.

Acceptance criteria
- Implement `classify_number(n: int) -> str` returning `'positive'|'negative'|'zero'`.
- Implement `is_leap_year(year: int) -> bool` following Gregorian rules.

Worked example

```py
def classify_number(n: int) -> str:
	if n > 0:
		return "positive"
	if n < 0:
		return "negative"
	# Lesson 02 — Conditionals and Boolean Logic

	Estimated time: 45–60 minutes

	Lesson goal
	- Teach how to write readable conditional logic using `if`/`elif`/`else` and boolean operators.
	- Practice common patterns: guard clauses, early returns, and small helper variables for clarity.

	Why this matters
	Conditional logic is the simplest form of decision-making in code. Clean, well-structured conditionals prevent bugs and make code easier to test and refactor. You'll use these patterns everywhere: input validation, feature flags, and route handling in web apps.

	Learning objectives
	- Write `if`/`elif`/`else` statements correctly.
	- Use comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) and boolean operators (`and`, `or`, `not`) clearly.
	- Apply guard clauses and conditional expressions where appropriate.

	Acceptance criteria
	- Implement `classify_number(n: int) -> str` returning one of `'positive'`, `'negative'`, or `'zero'`.
	- Implement `is_leap_year(year: int) -> bool` using the Gregorian rules (divisible by 4, except centuries not divisible by 400).

	Material and explanations

	1) Basic `if`/`elif`/`else`

	```py
	def classify_number(n: int) -> str:
		if n > 0:
			return "positive"
		if n < 0:
			return "negative"
		return "zero"
	```

	Note: prefer `if`/`elif`/`else` when branches are mutually exclusive — it documents intent.

	2) Boolean operators and clarity

	Complex boolean expressions quickly become hard to read. Break them into named helper variables:

	```py
	def is_valid_password(pw: str) -> bool:
		has_len = len(pw) >= 8
		has_digit = any(c.isdigit() for c in pw)
		has_alpha = any(c.isalpha() for c in pw)
		return has_len and has_digit and has_alpha
	```

	3) Leap year rules (worked example)

	```py
	def is_leap_year(year: int) -> bool:
		# divisible by 4
		if year % 4 != 0:
			return False
		# years divisible by 100 are not leap years unless divisible by 400
		if year % 100 == 0 and year % 400 != 0:
			return False
		return True

	# condensed but correct:
	def is_leap_year_compact(year: int) -> bool:
		return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
	```

	Testing note: include edge years: 1900 (not leap), 2000 (leap), 2024 (leap), 2023 (not leap).

	4) Guard clauses and early return

	Use guard clauses to reduce nesting and make the happy path clearer:

	```py
	def process(value: int) -> int:
		if value < 0:
			raise ValueError("value must be non-negative")
		# happy path continues without deep nesting
		return value * 2
	```

	5) Conditional expressions (ternary)

	```py
	status = "ok" if code == 200 else "error"
	```

	Real-world links
	- Conditionals and validation in web request handlers:
	  - FastAPI docs (request validation patterns): https://fastapi.tiangolo.com/tutorial/response-model/
	  - Flask request handling: https://flask.palletsprojects.com/en/latest/quickstart/#routing

	Exercises

	Mandatory
	1) Implement `classify_number(n: int) -> str` and `is_leap_year(year: int) -> bool`.
	2) Map a numeric `score` in 0..100 to a letter grade (`A`, `B`, `C`, `D`, `F`) using chained comparisons and return the letter.

	Optional
	- Implement `is_strong_password(pw: str) -> bool` as above and write tests.

	Hints & testing notes
	- For leap-year tests include 1900 (False) and 2000 (True).
	- When writing grade mapping, remember to validate the score range and raise `ValueError` for out-of-range values.

	How to run tests

	```powershell
	pytest -q "c:\\Projects\\python_lessions\\python_lessions\\basics\\lesson_02"
	```

	Further reading
	- Truthiness and short-circuiting: https://docs.python.org/3/reference/expressions.html#boolean-operations
	- Writing readable boolean expressions: https://realpython.com/python-boolean-operations/

	---

	If you want, I can also: 1) add `examples/run_demo.py` for this lesson, 2) write unit tests for the optional password validator, or 3) apply the same English template to the next lesson. Tell me which one to do next.
