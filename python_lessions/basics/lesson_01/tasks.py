"""
Tasks for Lesson 01
"""
from __future__ import annotations


def greeting(first_name: str, age: int) -> str:
    """Return a friendly greeting.

    Examples:
        greeting('Anna', 30) -> 'Hello, Anna! You are 30 years old.'
    """
    return f"Hello, {first_name}! You are {age} years old."


def rectangle_area(width: float, height: float) -> float:
    """Return area for rectangle. Raise ValueError for negative inputs."""
    if width < 0 or height < 0:
        raise ValueError("width and height must be non-negative")
    return float(width) * float(height)


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit (formula: C * 9/5 + 32)."""
    return float(celsius) * 9.0 / 5.0 + 32.0
