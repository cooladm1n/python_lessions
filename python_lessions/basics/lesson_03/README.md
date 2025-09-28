# Lesson 03: Loops (for/while), ranges, and loop patterns

Estimated time: 45-70 minutes

Learning outcomes
- Use `for`/`while` loops and `range` effectively.
- Apply loop control (`break`, `continue`) and use `enumerate`/`zip`.
- Implement accumulation patterns and simple algorithms (sum, factorial, prime check).

Acceptance criteria
- Implement `sum_range(n: int) -> int` returning sum 1..n.
- Implement `is_prime(n: int) -> bool` with simple trial division.

Worked examples

```py
def sum_range(n: int) -> int:
	total = 0
	for i in range(1, n+1):
		total += i
	return total

def is_prime(n: int) -> bool:
	if n < 2:
		return False
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True
```

Exercises (mandatory)
1) Implement `sum_range` and `is_prime` and write unit tests.
2) Compute dot product of two lists with `zip`.

Hints & testing
- Test `is_prime` on small primes and composites and edge inputs (0,1).
- For performance, trial division test only up to sqrt(n).
