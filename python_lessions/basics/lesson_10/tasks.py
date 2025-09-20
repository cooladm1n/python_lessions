"""
Tasks for Lesson 10 (Data Serialization)
"""
from __future__ import annotations
from pathlib import Path
from typing import Any, List, Dict


def save_json(data: Any, path: Path) -> None:
    raise NotImplementedError


def load_csv(path: Path) -> List[Dict[str, str]]:
    raise NotImplementedError


def serialize_data(obj: Any) -> Any:
    raise NotImplementedError


