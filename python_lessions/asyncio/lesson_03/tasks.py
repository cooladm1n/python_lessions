"""
Tasks for Lesson 03 (Async Iterators)
"""
from __future__ import annotations
from typing import AsyncIterator, List, TypeVar
import asyncio

T = TypeVar('T')


class AsyncRange:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step

    def __aiter__(self) -> AsyncRange:
        raise NotImplementedError

    async def __anext__(self) -> int:
        raise NotImplementedError


async def async_fibonacci() -> AsyncIterator[int]:
    raise NotImplementedError


async def async_batch(items: List[T], size: int) -> AsyncIterator[List[T]]:
    raise NotImplementedError


