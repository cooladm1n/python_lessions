# Lesson 04: Functions, Parameters, and Type Hints

In this lesson you will learn:
- Defining functions, returns, and early returns
- Positional, keyword, default, and keyword-only parameters
- `*args` and `**kwargs` for flexible APIs
- Type hints and docstrings for readability and tooling
- Pure functions vs side effects, input validation and errors

Guidelines:
- Keep functions small, focused, and named by intent.
- Validate inputs early; raise precise exceptions.
- Use keyword-only params for clarity in multi-flag functions.

Exercises:
1) Implement `greet(name: str, excited: bool=False)` that returns a string.
2) Implement `mean(*numbers: float) -> float` and test it.
3) Implement `clamp(value, *, min_value=None, max_value=None)` with validation.
4) Write `safe_div(a: float, b: float, *, default=None)` that returns `default` instead of raising on zero division.
5) Add type hints and docstrings to your functions and run a type checker.
6) Show multiple returns (tuple) and tuple unpacking.
7) Use a keyword-only boolean flag to change behavior clearly.
