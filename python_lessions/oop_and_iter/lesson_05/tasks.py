"""
Tasks for Lesson 05 (Magic Methods)
"""
from __future__ import annotations
from typing import Dict, Any


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        raise NotImplementedError

    def __mul__(self, scalar: float) -> Vector:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def __eq__(self, other: BankAccount) -> bool:
        raise NotImplementedError

    def __lt__(self, other: BankAccount) -> bool:
        raise NotImplementedError


class Counter:
    def __init__(self):
        self._data: Dict[str, int] = {}

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, key: str) -> int:
        raise NotImplementedError

    def __setitem__(self, key: str, value: int) -> None:
        raise NotImplementedError


