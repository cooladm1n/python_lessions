"""
Tasks for Lesson 07 (Context Managers)
"""
from __future__ import annotations
from contextlib import contextmanager
from pathlib import Path
from time import perf_counter
from typing import Optional


class Timer:
    def __init__(self):
        self.start_time: Optional[float] = None
        self.duration: Optional[float] = None

    def __enter__(self) -> Timer:
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError


class FileLock:
    def __init__(self, path: Path):
        self.path = path
        self.lock_file = path.with_suffix('.lock')

    def __enter__(self) -> FileLock:
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError


class DatabaseConnection:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connection = None

    def __enter__(self) -> DatabaseConnection:
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError


