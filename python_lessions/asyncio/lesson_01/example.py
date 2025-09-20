"""
Lesson 11: Asyncio Basics
"""
import asyncio
from time import sleep

async def fetch(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} done after {delay}s"

async def run_concurrent():
    tasks = [fetch("A", 0.5), fetch("B", 0.5), fetch("C", 0.5)]
    results = await asyncio.gather(*tasks)
    print(results)

async def offload_blocking():
    def blocking_work(x: int) -> int:
        sleep(0.2)  # simulate CPU/blocking
        return x * x
    results = await asyncio.gather(
        asyncio.to_thread(blocking_work, 3),
        asyncio.to_thread(blocking_work, 4),
    )
    print("offloaded:", results)

async def main():
    await run_concurrent()
    await offload_blocking()

if __name__ == "__main__":
    asyncio.run(main())
