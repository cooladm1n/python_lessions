"""
Tasks for Lesson 08 (Test Automation and CI/CD)
"""
from __future__ import annotations
from typing import Dict, Any, List, Callable, Optional
from enum import Enum


class TestStatus(Enum):
    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"
    ERROR = "error"


class TestRunner:
    def __init__(self):
        self.tests: List[Callable[..., Any]] = []
        self.results: List[Dict[str, Any]] = []
        self.parallel = False

    def add_test(self, test_func: Callable[..., Any]) -> None:
        raise NotImplementedError

    def set_parallel(self, parallel: bool) -> None:
        raise NotImplementedError

    async def run_tests(self) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def get_summary(self) -> Dict[str, int]:
        raise NotImplementedError


class CIPipeline:
    def __init__(self, pipeline_name: str):
        self.pipeline_name = pipeline_name
        self.stages: List[Dict[str, Any]] = []
        self.status: str = "pending"

    def add_stage(self, stage_name: str, commands: List[str]) -> None:
        raise NotImplementedError

    async def run_pipeline(self) -> Dict[str, Any]:
        raise NotImplementedError

    def get_pipeline_status(self) -> str:
        raise NotImplementedError


class TestNotification:
    def __init__(self):
        self.notifications: List[Dict[str, Any]] = []
        self.channels: List[str] = []

    def add_channel(self, channel: str) -> None:
        raise NotImplementedError

    def send_notification(self, message: str, level: str = "info") -> None:
        raise NotImplementedError

    def get_notifications(self) -> List[Dict[str, Any]]:
        raise NotImplementedError


