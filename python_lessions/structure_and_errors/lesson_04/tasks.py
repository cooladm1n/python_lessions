from __future__ import annotations
from pathlib import Path


def read_text_safe(path: Path) -> str:
    raise NotImplementedError


def write_text_safe(path: Path, text: str) -> None:
    raise NotImplementedError


def append_line(path: Path, line: str) -> None:
    raise NotImplementedError


