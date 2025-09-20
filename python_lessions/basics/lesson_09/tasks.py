"""
Tasks for Lesson 09 (Files and Directories)
"""
from __future__ import annotations
from pathlib import Path
from typing import List, Optional


def find_files(directory: Path, pattern: str) -> List[Path]:
    raise NotImplementedError


def copy_file(src: Path, dst: Path) -> None:
    raise NotImplementedError


def get_file_size(path: Path) -> Optional[int]:
    raise NotImplementedError


