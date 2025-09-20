"""
Lesson 09: OOP and Dataclasses
"""
from __future__ import annotations
from dataclasses import dataclass, field
from math import hypot
from typing import ClassVar

class BankAccount:
    bank_name: ClassVar[str] = "PyBank"

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("initial balance must be non-negative")
        self._owner = owner
        self._balance = balance

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0 or amount > self._balance:
            raise ValueError("invalid withdrawal amount")
        self._balance -= amount

    @classmethod
    def from_owner(cls, owner: str) -> "BankAccount":
        return cls(owner, 0.0)

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self.balance:.2f})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BankAccount):
            return NotImplemented
        return (self.owner, self.balance) == (other.owner, other.balance)

    def __lt__(self, other: "BankAccount") -> bool:
        return self.balance < other.balance

@dataclass(frozen=True, order=True)
class Point:
    x: float = field(compare=True)
    y: float = field(compare=True)

    def distance_to_origin(self) -> float:
        return hypot(self.x, self.y)

acct = BankAccount("Alice", 100)
acct.deposit(50)
print(acct)

p = Point(3, 4)
print("distance:", p.distance_to_origin())

# Sorting accounts by balance
accounts = [BankAccount("Bob", 20), BankAccount("Carol", 200), BankAccount("Dave", 150)]
for a in sorted(accounts):
    print(a)
