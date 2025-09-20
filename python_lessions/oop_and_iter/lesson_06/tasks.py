"""
Tasks for Lesson 06 (Advanced Iterators)
"""
from __future__ import annotations
from typing import Iterator, List, TypeVar

T = TypeVar('T')


class Range:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self) -> Iterator[int]:
        raise NotImplementedError

    def __next__(self) -> int:
        raise NotImplementedError


def fibonacci() -> Iterator[int]:
    raise NotImplementedError


def batch(items: List[T], size: int) -> Iterator[List[T]]:
    raise NotImplementedError


