"""
Tasks for Lesson 03 (Advanced Class Design)
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self) -> str:
        raise NotImplementedError


class Dog(Animal):
    def make_sound(self) -> str:
        raise NotImplementedError


class Cat(Animal):
    def make_sound(self) -> str:
        raise NotImplementedError


class Zoo:
    def __init__(self):
        self.animals: List[Animal] = []

    def add_animal(self, animal: Animal) -> None:
        raise NotImplementedError

    def make_all_sounds(self) -> List[str]:
        raise NotImplementedError


