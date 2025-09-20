# Lesson 09: Object-Oriented Programming (Classes and Dataclasses)

In this lesson you will learn:
- Defining classes, attributes, and methods
- Special methods `__init__`, `__repr__`, `__eq__`, ordering
- Encapsulation and properties with `@property`
- Using `@dataclass` for concise, immutable models
- Class vs instance attributes; class methods and static methods

Exercises:
1) Create a class `BankAccount` with deposit/withdraw and balance; validate inputs.
2) Use `@dataclass` for an immutable `Point(x, y)` with distance method.
3) Add `@property` to compute a derived attribute (e.g., full name).
4) Implement ordering by balance for `BankAccount` and sort accounts.
5) Add `@classmethod` constructor for `BankAccount.from_owner(owner)` with default balance.
6) Discuss when to freeze dataclasses and why.
