"""
Tasks for Lesson 07 (Async HTTP)
"""
from __future__ import annotations
import asyncio
from typing import Dict, Any, List, Optional
from urllib.parse import urljoin


class AsyncHttpClient:
    def __init__(self, base_url: str = ""):
        self.base_url = base_url
        self.session = None

    async def __aenter__(self) -> AsyncHttpClient:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError

    async def get(self, url: str, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError

    async def post(self, url: str, data: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError


class AsyncWebScraper:
    def __init__(self, max_concurrent: int = 5):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def scrape_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        raise NotImplementedError

    async def scrape_single(self, url: str) -> Dict[str, Any]:
        raise NotImplementedError


class AsyncRateLimitedClient:
    def __init__(self, rate_limit: int, per_second: float):
        self.rate_limit = rate_limit
        self.per_second = per_second
        self.rate_limiter = None

    async def __aenter__(self) -> AsyncRateLimitedClient:
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError

    async def request(self, method: str, url: str, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError


