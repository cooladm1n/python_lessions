from __future__ import annotations

"""
Tasks for Lesson 03: Loops
"""


def sum_range(n: int) -> int:
    """Return sum of numbers from 1 to n (inclusive)."""
    if n <= 0:
        return 0
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def is_prime(n: int) -> bool:
    """Return True if n is a prime (simple trial division)."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
 

def count_evens(values: list[int]) -> int:
    """Return number of even ints in values."""
    return sum(1 for x in values if x % 2 == 0)
