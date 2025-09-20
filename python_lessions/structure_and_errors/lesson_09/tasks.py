from __future__ import annotations
import os
from typing import Optional


def get_env(name: str, default: Optional[str] = None) -> Optional[str]:
    raise NotImplementedError


def resolve_port(env: dict[str, str], config: dict[str, int], default: int) -> int:
    raise NotImplementedError


def bool_env(name: str, default: bool = False) -> bool:
    raise NotImplementedError


