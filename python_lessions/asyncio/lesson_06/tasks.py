"""
Tasks for Lesson 06 (Async Error Handling)
"""
from __future__ import annotations
import asyncio
from typing import Callable, Any, Optional
from enum import Enum


class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


def async_retry(max_attempts: int, delay: float):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        raise NotImplementedError
    return decorator


class AsyncCircuitBreaker:
    def __init__(self, failure_threshold: int, timeout: float):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time: Optional[float] = None
        self.state = CircuitState.CLOSED

    async def call(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        raise NotImplementedError


class AsyncTimeout:
    def __init__(self, timeout: float):
        self.timeout = timeout
        self.task: Optional[asyncio.Task] = None

    async def __aenter__(self) -> AsyncTimeout:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError


