"""
Lesson 04: Functions and Type Hints
"""
from __future__ import annotations
from typing import Iterable, Optional, Tuple, Any


def greet(name: str, excited: bool = False) -> str:
    """Return a friendly greeting.

    Args:
        name: Person's name.
        excited: Whether to add excitement.
    """
    ending = "!!!" if excited else "."
    return f"Hello, {name}{ending}"


def mean(numbers: Iterable[float]) -> float:
    """Compute arithmetic mean of an iterable of numbers."""
    values = list(numbers)
    if not values:
        raise ValueError("mean() of empty iterable")
    return sum(values) / len(values)


def clamp(value: float, *, min_value: Optional[float] = None, max_value: Optional[float] = None) -> float:
    """Clamp value into [min_value, max_value] if bounds are provided."""
    result = value
    if min_value is not None and result < min_value:
        result = min_value
    if max_value is not None and result > max_value:
        result = max_value
    return result


def safe_div(a: float, b: float, *, default: Optional[float] = None) -> Optional[float]:
    """Return a/b, or `default` if b==0 instead of raising.

    Prefer explicit handling over hiding real errors in larger programs.
    """
    if b == 0:
        return default
    return a / b


def split_name(full_name: str) -> Tuple[str, str]:
    """Return (first, last) for a two-part name."""
    first, last = full_name.strip().split(" ", 1)
    return first, last

print(greet("Alice"))
print(greet("Bob", excited=True))
print("mean:", mean([1, 2, 3, 4]))
print("clamp:", clamp(15, min_value=0, max_value=10))
print("safe_div:", safe_div(1, 0, default=float("inf")))

first, last = split_name("Ada Lovelace")
print("first:", first, "last:", last)
