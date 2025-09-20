from __future__ import annotations
from pathlib import Path
from contextlib import suppress, contextmanager
from typing import Optional


def silent_remove(path: Path) -> None:
    raise NotImplementedError


def try_parse_int(s: str, default: Optional[int] = None) -> Optional[int]:
    raise NotImplementedError

@contextmanager
def timeout(seconds: float):
    # simple emulation context (no real thread cancel): record time and warn if too long
    raise NotImplementedError


