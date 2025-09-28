from __future__ import annotations

"""
Tasks for Lesson 04: Functions and Type Hints
"""


def greet(name: str, excited: bool = False) -> str:
    """Return greeting. If excited True, add exclamation."""
    return f"Hello, {name}{'!!!' if excited else '.'}"


def mean(*numbers: float) -> float:
    """Return arithmetic mean of numbers; raise ValueError on empty input."""
    # Support calling mean(1,2,3) or mean([1,2,3])
    if len(numbers) == 0:
        raise ValueError("mean requires at least one number")

    if len(numbers) == 1 and isinstance(numbers[0], (list, tuple, set, range)):
        seq = list(numbers[0])
    else:
        seq = list(numbers)

    if len(seq) == 0:
        raise ValueError("mean requires at least one number")

    return sum(seq) / len(seq)


def clamp(value: float, *, min_value: float | None = None, max_value: float | None = None) -> float:
    """Clamp value between optional min_value and max_value."""
    if min_value is not None and value < min_value:
        return min_value
    if max_value is not None and value > max_value:
        return max_value
    return value
 
