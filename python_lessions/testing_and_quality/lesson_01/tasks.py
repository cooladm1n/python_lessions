"""
Tasks for Lesson 12
"""
from __future__ import annotations


def add(a: int, b: int) -> int:
    """Return sum of two integers."""
    return a + b


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


def normalize_whitespace(s: str) -> str:
    """Collapse multiple whitespace chars into single spaces and strip ends."""
    import re

    return re.sub(r"\s+", " ", s).strip()
