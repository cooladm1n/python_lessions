"""
Tasks for Lesson 05 (Async Semaphores and Rate Limiting)
"""
from __future__ import annotations
import asyncio
from typing import Callable, Any
from time import time


class RateLimiter:
    def __init__(self, rate: int, per: float):
        self.rate = rate
        self.per = per
        self.tokens = rate
        self.last_update = time()

    async def acquire(self) -> None:
        raise NotImplementedError


class AsyncSemaphore:
    def __init__(self, value: int, timeout: float = None):
        self.semaphore = asyncio.Semaphore(value)
        self.timeout = timeout

    async def acquire(self) -> bool:
        raise NotImplementedError

    async def release(self) -> None:
        raise NotImplementedError


class ConcurrentExecutor:
    def __init__(self, max_concurrent: int):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def execute(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        raise NotImplementedError


