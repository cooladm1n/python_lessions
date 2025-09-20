import asyncio
import time
from tasks import RateLimiter, AsyncSemaphore, ConcurrentExecutor


async def test_rate_limiter():
    limiter = RateLimiter(2, 1.0)  # 2 requests per second
    
    start = time.time()
    await limiter.acquire()
    await limiter.acquire()
    await limiter.acquire()  # Should be rate limited
    elapsed = time.time() - start
    
    assert elapsed >= 1.0  # Should have waited at least 1 second


async def test_async_semaphore():
    semaphore = AsyncSemaphore(2)
    
    acquired = await semaphore.acquire()
    assert acquired is True
    
    acquired = await semaphore.acquire()
    assert acquired is True
    
    # Third acquire should fail with timeout
    acquired = await semaphore.acquire()
    assert acquired is False


async def test_concurrent_executor():
    executor = ConcurrentExecutor(2)
    
    async def slow_task(delay: float) -> str:
        await asyncio.sleep(delay)
        return f"completed after {delay}s"
    
    # Start 3 tasks, but only 2 should run concurrently
    tasks = [
        executor.execute(slow_task, 0.1),
        executor.execute(slow_task, 0.1),
        executor.execute(slow_task, 0.1)
    ]
    
    results = await asyncio.gather(*tasks)
    assert len(results) == 3


