"""
Tasks for Lesson 10
"""
from __future__ import annotations
from contextlib import contextmanager
from time import perf_counter
from itertools import islice


def fib():
    raise NotImplementedError


def first_n_fibs(n: int) -> list[int]:
    raise NotImplementedError

@contextmanager
def timer():
    start = perf_counter()
    try:
        yield
    finally:
        # keep side-effect printing for tests
        print(f"took {perf_counter() - start:.6f}s")
