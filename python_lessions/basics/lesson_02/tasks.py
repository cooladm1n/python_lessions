from __future__ import annotations

"""
Tasks for Lesson 02: Conditions and Boolean Logic
"""


def classify_number(n: int) -> str:
    """Return 'positive', 'negative', or 'zero' for integer n."""
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"


def is_leap_year(year: int) -> bool:
    """Return True for Gregorian leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
 

def grade(score: int) -> str:
    """Map score 0..100 to letter grade A..F."""
    if not (0 <= score <= 100):
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
