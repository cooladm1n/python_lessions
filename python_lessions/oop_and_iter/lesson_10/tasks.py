"""
Tasks for Lesson 10 (Advanced Data Structures)
"""
from __future__ import annotations
from typing import Optional, Any, Dict


class Stack:
    def __init__(self):
        self._items: list = []

    def push(self, item: Any) -> None:
        raise NotImplementedError

    def pop(self) -> Any:
        raise NotImplementedError

    def peek(self) -> Optional[Any]:
        raise NotImplementedError


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache: Dict[str, Any] = {}
        self._order: list = []

    def get(self, key: str) -> Optional[Any]:
        raise NotImplementedError

    def put(self, key: str, value: Any) -> None:
        raise NotImplementedError


class Trie:
    def __init__(self):
        self._root: Dict[str, Any] = {}

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def starts_with(self, prefix: str) -> bool:
        raise NotImplementedError


