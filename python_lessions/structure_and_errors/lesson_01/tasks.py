"""
Tasks for Lesson 07
"""
from __future__ import annotations

class NegativeAmountError(ValueError):
    pass

def safe_div(a: float, b: float, *, default=None):
    raise NotImplementedError

def parse_int(s: str) -> int:
    raise NotImplementedError

def deposit(balance: float, amount: float) -> float:
    raise NotImplementedError
