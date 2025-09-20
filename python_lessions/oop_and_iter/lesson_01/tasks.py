"""
Tasks for Lesson 09
"""
from __future__ import annotations
from dataclasses import dataclass
from math import hypot
from typing import ClassVar


class BankAccount:
    bank_name: ClassVar[str] = "PyBank"

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        raise NotImplementedError

    @property
    def balance(self) -> float:
        raise NotImplementedError

    def deposit(self, amount: float) -> None:
        raise NotImplementedError

    def withdraw(self, amount: float) -> None:
        raise NotImplementedError


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to_origin(self) -> float:
        raise NotImplementedError
