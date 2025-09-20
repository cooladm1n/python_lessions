"""
Tasks for Lesson 04 (Async Queues)
"""
from __future__ import annotations
import asyncio
from typing import Any, List


class AsyncProducer:
    def __init__(self, queue: asyncio.Queue, items: List[Any]):
        self.queue = queue
        self.items = items

    async def produce(self) -> None:
        raise NotImplementedError


class AsyncConsumer:
    def __init__(self, queue: asyncio.Queue):
        self.queue = queue
        self.processed_items: List[Any] = []

    async def consume(self) -> None:
        raise NotImplementedError


class AsyncPipeline:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.producer = None
        self.consumer = None

    def add_producer(self, producer: AsyncProducer) -> None:
        raise NotImplementedError

    def add_consumer(self, consumer: AsyncConsumer) -> None:
        raise NotImplementedError

    async def run(self) -> None:
        raise NotImplementedError


