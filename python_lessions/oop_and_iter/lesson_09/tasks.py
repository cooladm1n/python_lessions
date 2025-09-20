"""
Tasks for Lesson 09 (Functional Programming)
"""
from __future__ import annotations
from typing import Callable, Any


def compose(f: Callable[[Any], Any], g: Callable[[Any], Any]) -> Callable[[Any], Any]:
    raise NotImplementedError


def partial_apply(func: Callable[..., Any], *args: Any) -> Callable[..., Any]:
    raise NotImplementedError


def pipe(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    raise NotImplementedError


