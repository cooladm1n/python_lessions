# Lesson 01 — Getting Started with Python

Estimated time: 45–60 minutes

Lesson goal
- Give the student practical understanding of basic types and the structure of simple Python programs.
- Teach how to write small, well-typed functions with short docstrings.

What's covered in this lesson (short)
- How a Python script is structured: files, entry point, running with the interpreter.
- Primitive types: int, float, str, bool, None.
- Arithmetic, division vs integer division, operator precedence.
- String formatting (f-strings).
- Basic error handling and input validation.

Why this matters
In real projects (web backends, automation, data processing), you'll frequently convert data between types, validate inputs, and compose small functions into modules. Solid basics reduce bugs and make your code easier to test and maintain.

Learning objectives (concrete)
- Run a script and explain what a function is and how a function call works.
- Distinguish numbers and strings; know when to cast explicitly.
- Write functions with type annotations and docstrings.

Acceptance criteria (what tests will check)
- Implement `greeting(first_name: str, age: int) -> str` — returns a polite message.
- Implement `rectangle_area(width: float, height: float) -> float` — computes area; raises `ValueError` on negative inputs.
- Implement `celsius_to_fahrenheit(celsius: float) -> float` — correct conversion formula (0.01 tolerance in tests).

Material and explanations

1) Running a Python script
- Run a `.py` file:

```powershell
python path\\to\\script.py
```

- In this repository each lesson has a `tasks.py` where you implement functions. Tests use `pytest`.

2) Primitive types (brief)
- int — integers: 0, -3, 42
- float — floats: 3.14, -0.5
- str — strings: "hello"
- bool — True / False
- None — missing/empty value

Example: casting and pitfalls

```py
age_str = "30"
age_int = int(age_str)  # explicit cast
bad = "30a"
# int(bad) -> ValueError
```

3) Division: `/` vs `//`
- `/` returns a float: `7 / 2 == 3.5`.
- `//` is floor (integer) division. Note negative values:

```py
7 // 2   # -> 3
-7 // 2  # -> -4  (floor)
```

Explanation: `//` rounds down (towards -inf), not truncation by sign—this surprises many beginners.

4) f-strings

```py
name = "Anna"
age = 30
msg = f"Hello, {name}! You are {age} years old."
```

Prefer returning values from functions instead of printing; printing is for demos.

5) Input validation
- Check function inputs and raise `ValueError` (or `TypeError`) for invalid data. This makes functions predictable and testable.

Worked examples (live code)

greeting

```py
def greeting(first_name: str, age: int) -> str:
    """Return a friendly greeting message.

    Notes:
    - Keep the function pure: return a string, don't print inside the function.
    - Add a short docstring explaining inputs and behavior.
    """
    return f"Hello, {first_name}! You are {age} years old."

print(greeting("Anna", 30))
```

rectangle_area

```py
def rectangle_area(width: float, height: float) -> float:
    """Return area of rectangle. Raise ValueError for negative sizes."""
    if width < 0 or height < 0:
        raise ValueError("width and height must be non-negative")
    return width * height

print(rectangle_area(3.0, 4.0))  # 12.0
```

celsius_to_fahrenheit

```py
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5.0 + 32.0

print(round(celsius_to_fahrenheit(0), 2))  # 32.0
```

Real-world examples and links
- Casting and validation are common in web forms and API handlers. See how request parsing/validation is implemented in Flask/Django:
  - Flask quickstart: https://flask.palletsprojects.com/en/latest/quickstart/#a-minimal-application
  - Django forms & validation: https://docs.djangoproject.com/en/stable/ref/forms/fields/
- Type annotations and small utilities in a real project: httpx (HTTP client): https://github.com/encode/httpx

Notes and footnotes
- Tests in this course verify function return values. Avoid using `print` inside functions under test.
- Use `if __name__ == "__main__":` blocks for demo scripts.
- Keep computation logic separate from side effects (I/O, printing) to make testing easier.

Exercises

Mandatory
1) Implement three functions in `tasks.py`: `greeting`, `rectangle_area`, `celsius_to_fahrenheit` according to acceptance criteria.
2) Create a short example that demonstrates the difference between `/` and `//` for `7` and `-7` and add a comment explaining the result.

Optional
- Add stricter type validation to `rectangle_area` (use `isinstance`) and write a test that passing a string raises `TypeError`.
- Create `examples/run_demo.py` that prints a few usage examples (useful for manual testing).

How to check your work
- Run tests for the lesson:

```powershell
pytest -q "c:\\Projects\\python_lessions\\python_lessions\\basics\\lesson_01"
```

- Try the worked examples locally to see the output.

Further reading
- Official Python tutorial: https://docs.python.org/3/tutorial/
- Type hints guide: https://peps.python.org/pep-0484/

---

If you want, I can: 1) add `examples/run_demo.py` for this lesson, 2) apply the README template automatically to remaining lessons, or 3) write tests for stricter type validation. Tell me which to do next.
