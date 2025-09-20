from __future__ import annotations
import logging
from typing import Callable, Any


def get_logger(name: str) -> logging.Logger:
    raise NotImplementedError


def log_start_stop(logger: logging.Logger) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    raise NotImplementedError


def log_exception(logger: logging.Logger) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    raise NotImplementedError


