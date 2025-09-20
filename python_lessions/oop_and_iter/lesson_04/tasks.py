"""
Tasks for Lesson 04 (Property Decorators)
"""
from __future__ import annotations
from datetime import datetime


class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        raise NotImplementedError

    @celsius.setter
    def celsius(self, value: float) -> None:
        raise NotImplementedError


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        raise NotImplementedError

    @property
    def perimeter(self) -> float:
        raise NotImplementedError


class Person:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self._birth_year = birth_year

    @property
    def age(self) -> int:
        raise NotImplementedError

    @age.setter
    def age(self, value: int) -> None:
        raise NotImplementedError


