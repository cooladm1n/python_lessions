"""
Tasks for Lesson 09 (Async Testing)
"""
from __future__ import annotations
import asyncio
from typing import Callable, Any, Dict, List
from unittest.mock import AsyncMock as BaseAsyncMock


class AsyncMock:
    def __init__(self, return_value: Any = None, side_effect: Exception = None):
        self.return_value = return_value
        self.side_effect = side_effect
        self.call_count = 0
        self.call_args_list: List[tuple] = []

    async def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    def assert_called_once_with(self, *args, **kwargs) -> None:
        raise NotImplementedError


class AsyncTestRunner:
    def __init__(self):
        self.tests: List[Callable[..., Any]] = []
        self.results: List[Dict[str, Any]] = []

    def add_test(self, test_func: Callable[..., Any]) -> None:
        raise NotImplementedError

    async def run_tests(self) -> List[Dict[str, Any]]:
        raise NotImplementedError


class AsyncFixture:
    def __init__(self, setup_func: Callable[..., Any], teardown_func: Callable[..., Any] = None):
        self.setup_func = setup_func
        self.teardown_func = teardown_func
        self.value: Any = None

    async def __aenter__(self) -> Any:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError


