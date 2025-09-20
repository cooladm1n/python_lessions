"""
Tasks for Lesson 07 (Integration Testing)
"""
from __future__ import annotations
from typing import Dict, Any, List, Callable, Optional
from unittest.mock import Mock


class IntegrationTestSuite:
    def __init__(self):
        self.tests: List[Callable[..., Any]] = []
        self.results: List[Dict[str, Any]] = []
        self.setup_func: Optional[Callable[..., Any]] = None
        self.teardown_func: Optional[Callable[..., Any]] = None

    def add_test(self, test_func: Callable[..., Any]) -> None:
        raise NotImplementedError

    def set_setup(self, setup_func: Callable[..., Any]) -> None:
        raise NotImplementedError

    def set_teardown(self, teardown_func: Callable[..., Any]) -> None:
        raise NotImplementedError

    async def run_tests(self) -> List[Dict[str, Any]]:
        raise NotImplementedError


class ServiceMock:
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.endpoints: Dict[str, Mock] = {}
        self.call_logs: List[Dict[str, Any]] = []

    def mock_endpoint(self, endpoint: str, response: Any) -> None:
        raise NotImplementedError

    def get_call_logs(self) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def reset(self) -> None:
        raise NotImplementedError


class DatabaseTestHelper:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connection = None
        self.test_data: List[Dict[str, Any]] = []

    async def setup(self) -> None:
        raise NotImplementedError

    async def teardown(self) -> None:
        raise NotImplementedError

    async def insert_test_data(self, data: Dict[str, Any]) -> None:
        raise NotImplementedError

    async def get_test_data(self) -> List[Dict[str, Any]]:
        raise NotImplementedError


