# Lesson 03: Loops (for/while), ranges, and loop patterns

In this lesson you will learn:
- Iteration with `for` and `while`
- Using `range(start, stop, step)`
- `break`, `continue`, and `else` on loops
- Accumulation patterns: sum, count, min/max, factorial
- Iterating with `enumerate` and `zip`

Guidance:
- Prefer `for` when iterating over known sequences; `while` for open-ended loops.
- Use `enumerate(seq, start=1)` to get indexes without manual counters.
- Loop `else` executes when the loop wasn't terminated by `break`.

Exercises:
1) Sum numbers 1..100 using a loop.
2) Print a multiplication table 1..5.
3) Given a list of ints, count how many are even and compute their sum.
4) Check if a number is prime using a loop and `break`+`else`.
5) Find the smallest and largest values in a list without using `min`/`max`.
6) Use `enumerate` to print line numbers for a list of strings.
7) Iterate two lists in parallel with `zip` to compute dot product.
8) Use a `while` loop to compute factorial of `n`.
9) Show how `continue` skips odd numbers.
10) Explain when you would use `while True` with a `break`.
