"""
Tasks for Lesson 09 (Test Data Management)
"""
from __future__ import annotations
from typing import Dict, Any, List, Optional
from pathlib import Path


class TestDataManager:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.data_sets: Dict[str, List[Dict[str, Any]]] = {}

    def load_data_set(self, name: str, file_path: Path) -> None:
        raise NotImplementedError

    def get_data_set(self, name: str) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def create_data_set(self, name: str, data: List[Dict[str, Any]]) -> None:
        raise NotImplementedError

    def cleanup_data(self) -> None:
        raise NotImplementedError


class TestEnvironment:
    def __init__(self, env_name: str):
        self.env_name = env_name
        self.config: Dict[str, Any] = {}
        self.services: List[str] = []

    def set_config(self, key: str, value: Any) -> None:
        raise NotImplementedError

    def add_service(self, service: str) -> None:
        raise NotImplementedError

    async def setup(self) -> None:
        raise NotImplementedError

    async def teardown(self) -> None:
        raise NotImplementedError


class DataGenerator:
    def __init__(self):
        self.generators: Dict[str, Callable[..., Any]] = {}

    def add_generator(self, name: str, generator_func: Callable[..., Any]) -> None:
        raise NotImplementedError

    def generate_data(self, name: str, count: int) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def generate_user_data(self, count: int) -> List[Dict[str, Any]]:
        raise NotImplementedError


