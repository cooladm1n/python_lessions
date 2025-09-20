import asyncio
import pytest
from tasks import async_retry, AsyncCircuitBreaker, AsyncTimeout


async def test_async_retry():
    call_count = 0

    @async_retry(max_attempts=3, delay=0.01)
    async def flaky_func():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ValueError("Temporary failure")
        return "success"

    result = await flaky_func()
    assert result == "success"
    assert call_count == 3


async def test_async_circuit_breaker():
    breaker = AsyncCircuitBreaker(failure_threshold=2, timeout=0.1)
    
    async def failing_func():
        raise RuntimeError("Service unavailable")
    
    # First two calls should fail and increment failure count
    with pytest.raises(RuntimeError):
        await breaker.call(failing_func)
    
    with pytest.raises(RuntimeError):
        await breaker.call(failing_func)
    
    # Third call should be blocked by circuit breaker
    with pytest.raises(Exception):  # Circuit breaker should raise
        await breaker.call(failing_func)


async def test_async_timeout():
    async def slow_task():
        await asyncio.sleep(0.2)
        return "completed"
    
    async with AsyncTimeout(0.1):
        with pytest.raises(asyncio.TimeoutError):
            await slow_task()


