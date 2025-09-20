# Lesson 02: Conditions (if/elif/else) and Boolean Logic

In this lesson you will learn:
- Branching with `if`, `elif`, and `else`
- Comparison operators: `== != < <= > >=`
- Boolean operators: `and`, `or`, `not`
- Truthiness of values and guard clauses
- Chained comparisons: `0 <= x < 10`
- Conditional expressions (ternary): `a if cond else b`

Best practices:
- Use guard clauses to return early when invalid input is detected.
- Keep conditions readable: extract complex checks into well-named variables.
- Prefer explicit comparisons over relying on truthiness for numbers.

Exercises:
1) Given `n`, print whether it is positive, negative, or zero.
2) Determine if a year is a leap year (divisible by 4, not by 100 unless by 400).
3) Print the largest of three numbers without using `max`.
4) Given `score` 0..100, map to a letter grade with thresholds.
5) Validate a password: length >= 8 and contains a digit and a letter.
6) Use a conditional expression to set `status` to `"adult"` or `"minor"`.
7) Demonstrate chained comparison: `if 0 <= x <= 100`.
8) Show De Morgan's laws with examples and verify equivalence.
9) Explain why `if x:` may be misleading when `x` can be `0` or empty.
10) Protect a division with a guard clause; compare to nested `if`s.
