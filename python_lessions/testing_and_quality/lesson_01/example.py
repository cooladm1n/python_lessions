"""
Lesson 12: Testing and Best Practices
"""
from __future__ import annotations


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b

# Simple inline tests (demo): prefer pytest/unittest for real projects
if __name__ == "__main__":
    # Arrange
    a, b = 2, 2
    # Act
    s = add(a, b)
    d = subtract(a, b)
    # Assert
    assert s == 4
    assert d == 0
    print("tests passed")
