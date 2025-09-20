"""
Tasks for Lesson 02 (Async Context Managers)
"""
from __future__ import annotations
from pathlib import Path
from typing import Optional


class AsyncFile:
    def __init__(self, path: Path, mode: str = "r"):
        self.path = path
        self.mode = mode
        self.file = None

    async def __aenter__(self) -> AsyncFile:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError

    async def read(self) -> str:
        raise NotImplementedError

    async def write(self, content: str) -> None:
        raise NotImplementedError


class AsyncDatabase:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connection = None

    async def __aenter__(self) -> AsyncDatabase:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError

    async def execute(self, query: str) -> list:
        raise NotImplementedError


class AsyncLock:
    def __init__(self):
        self._locked = False

    async def __aenter__(self) -> AsyncLock:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError


