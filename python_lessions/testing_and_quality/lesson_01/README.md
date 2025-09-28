# Lesson 12: Testing, Type Checking, and Best Practices

Estimated time: 60-120 minutes

Learning outcomes
- Write unit tests with `pytest` (including parametrized tests and fixtures).
- Use type hints and run `mypy` for basic static checks.
- Apply code formatting (`black`, `isort`) and basic linting.
- Design tests following AAA (Arrange-Act-Assert) and add meaningful edge-case tests.

Acceptance criteria
- Implement `add(a,b)`, `is_even(n)`, and `normalize_whitespace(s)` in `tasks.py`.
- Provide tests in `test_tasks.py` that cover normal and edge cases.

Exercises (mandatory)
1) Write unit tests for the three functions and ensure they pass with pytest.
2) Add type hints and run a static type check (mypy) — fix obvious type mistakes.

Optional
- Add property-based tests for `is_even` using Hypothesis.

Testing notes
- Use `pytest` for running tests. Prefer small, fast, deterministic tests.
- Use fixtures for repeated setup (e.g., temporary files) and parametrization for multiple inputs.
