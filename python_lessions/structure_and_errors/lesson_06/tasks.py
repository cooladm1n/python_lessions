from __future__ import annotations
from typing import Any, Type


def parse_json(s: str) -> dict[str, Any]:
    raise NotImplementedError


def get_required(mapping: dict[str, Any], key: str, typ: Type[Any]) -> Any:
    raise NotImplementedError


def get_int_in_range(mapping: dict[str, Any], key: str, min_value: int, max_value: int) -> int:
    raise NotImplementedError


