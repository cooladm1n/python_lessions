# Lesson 01: Getting Started with Python

In this lesson you will learn:
- What a Python program looks like
- Variables and basic types: `int`, `float`, `str`, `bool`, `None`
- Arithmetic operators: `+ - * / // % **`
- Assignment, naming, and constants-by-convention
- Printing with f-strings and `str.format`
- Type conversion: `int()`, `float()`, `str()`, `bool()`
- Quick debugging with `type()` and `print()`

Key tips:
- Use clear variable names; prefer full words over abbreviations.
- Keep values immutable where possible; treat ALL_CAPS as constants by convention.
- Prefer f-strings for readability.

Examples you will run in `example.py`:
- Create and print variables of different types
- Compute areas/perimeters with arithmetic
- Demonstrate f-strings and formatting
- Show common pitfalls of integer vs float division

Exercises:
1) Create two variables `first_name` and `age`, then print a friendly greeting.
2) Compute the area and perimeter of a rectangle for width=7 and height=3.
3) Convert temperature: given `celsius=23.5`, print Fahrenheit with 2 decimals.
4) Show the difference between `/` and `//` for `7` and `-7`.
5) Given `price=19.99` and `qty=3`, compute a total and format as `$59.97`.
6) Use `bool()` to check truthiness of: `0`, `""`, `[]`, `[0]`, `"False"`.
7) Safely cast a string `"42"` to `int` and `float`. What about `"42.0"`?
8) Create `PI=3.14159` and compute circle area for `r=4`. Keep 3 decimals.
9) Print the types of several values using `type()` and explain results.
10) Explain what happens if you try `int("hello")` and why.

Going further:
- Read error messages carefully; they often tell you exactly what to fix.
- Keep code tidy and grouped by sections; comment high-level intent, not every line.
