# Lesson 04: Functions, Parameters, and Type Hints

Estimated time: 45-75 minutes

Learning outcomes
- Define functions with positional, keyword and keyword-only parameters.
- Use `*args`/`**kwargs`, docstrings and type hints.
- Distinguish pure functions from side-effecting ones and validate inputs.

Acceptance criteria
- Implement `greet(name: str, excited: bool=False) -> str`.
- Implement `mean(*numbers: float) -> float` raising ValueError on empty input.

Worked examples

```py
def greet(name: str, excited: bool = False) -> str:
	return f"Hello, {name}{'!' if excited else '.'}"

def mean(*numbers: float) -> float:
	if not numbers:
		raise ValueError("mean requires at least one number")
	return sum(numbers) / len(numbers)
```

Exercises (mandatory)
1) Implement `greet` and `mean` and write tests for normal and error cases.
2) Implement `clamp(value, *, min_value=None, max_value=None)` that enforces bounds.

Hints & testing
- Use type hints and run `mypy` to catch simple mistakes.
- Write tests for keyword-only parameters to ensure correct behavior.
