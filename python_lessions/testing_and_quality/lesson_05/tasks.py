"""
Tasks for Lesson 05 (Performance Testing)
"""
from __future__ import annotations
import time
from typing import Dict, Any, List, Callable
from contextlib import contextmanager


class PerformanceProfiler:
    def __init__(self):
        self.profiles: Dict[str, List[float]] = {}
        self.current_profile: Optional[str] = None

    @contextmanager
    def profile(self, name: str):
        raise NotImplementedError

    def get_profile_stats(self, name: str) -> Dict[str, float]:
        raise NotImplementedError

    def get_all_profiles(self) -> Dict[str, Dict[str, float]]:
        raise NotImplementedError


class LoadTester:
    def __init__(self, target_url: str):
        self.target_url = target_url
        self.results: List[Dict[str, Any]] = []

    async def run_load_test(self, concurrent_users: int, duration: float) -> Dict[str, Any]:
        raise NotImplementedError

    def get_response_times(self) -> List[float]:
        raise NotImplementedError

    def get_error_rate(self) -> float:
        raise NotImplementedError


class BenchmarkRunner:
    def __init__(self):
        self.benchmarks: List[Callable[..., Any]] = []
        self.results: Dict[str, Dict[str, Any]] = {}

    def add_benchmark(self, name: str, func: Callable[..., Any]) -> None:
        raise NotImplementedError

    def run_benchmarks(self) -> Dict[str, Dict[str, Any]]:
        raise NotImplementedError

    def compare_benchmarks(self) -> str:
        raise NotImplementedError


