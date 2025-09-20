"""
Tasks for Lesson 08 (Async Database)
"""
from __future__ import annotations
import asyncio
from typing import Dict, Any, List, Optional
from contextlib import asynccontextmanager


class AsyncDatabase:
    def __init__(self, connection_string: str, pool_size: int = 10):
        self.connection_string = connection_string
        self.pool_size = pool_size
        self.pool = None

    async def __aenter__(self) -> AsyncDatabase:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError

    async def execute(self, query: str, params: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        raise NotImplementedError

    async def fetch_one(self, query: str, params: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        raise NotImplementedError


class AsyncTransaction:
    def __init__(self, db: AsyncDatabase):
        self.db = db
        self.connection = None

    async def __aenter__(self) -> AsyncTransaction:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError

    async def execute(self, query: str, params: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        raise NotImplementedError


class AsyncQueryBuilder:
    def __init__(self):
        self.query = ""
        self.params: Dict[str, Any] = {}

    def select(self, columns: List[str]) -> AsyncQueryBuilder:
        raise NotImplementedError

    def from_table(self, table: str) -> AsyncQueryBuilder:
        raise NotImplementedError

    def where(self, condition: str, value: Any) -> AsyncQueryBuilder:
        raise NotImplementedError

    def build(self) -> tuple[str, Dict[str, Any]]:
        raise NotImplementedError


