"""
Tasks for Lesson 08 (Decorators and Metaclasses)
"""
from __future__ import annotations
from typing import Callable, Any, Dict
from functools import wraps


def cached(func: Callable[..., Any]) -> Callable[..., Any]:
    raise NotImplementedError


def retry(max_attempts: int):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        raise NotImplementedError
    return decorator


class Singleton(type):
    _instances: Dict[type, Any] = {}

    def __call__(cls, *args, **kwargs) -> Any:
        raise NotImplementedError


