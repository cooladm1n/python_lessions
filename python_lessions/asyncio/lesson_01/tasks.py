"""
Tasks for Lesson 11
"""
from __future__ import annotations
import asyncio


async def fetch(name: str, delay: float) -> str:
    """Simulate a network fetch by awaiting asyncio.sleep(delay) then returning a message.

    Example return: "X done after 0.01"
    """
    await asyncio.sleep(delay)
    return f"{name} done after {delay}"


async def run_three() -> list[str]:
    """Run three fetch coroutines concurrently and return their results as a list."""
    tasks = [fetch("A", 0.01), fetch("B", 0.01), fetch("C", 0.01)]
    results = await asyncio.gather(*tasks)
    return results


async def offload_square(x: int) -> int:
    """Offload CPU-bound or blocking work to a thread with asyncio.to_thread and return x*x."""
    return await asyncio.to_thread(lambda: x * x)
