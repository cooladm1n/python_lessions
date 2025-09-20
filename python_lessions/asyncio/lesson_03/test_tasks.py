import asyncio
from tasks import AsyncRange, async_fibonacci, async_batch


async def test_async_range():
    r = AsyncRange(1, 5)
    numbers = []
    async for num in r:
        numbers.append(num)
    assert numbers == [1, 2, 3, 4]


async def test_async_fibonacci():
    fib = async_fibonacci()
    first_ten = []
    async for num in fib:
        first_ten.append(num)
        if len(first_ten) >= 10:
            break
    assert first_ten == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


async def test_async_batch():
    items = [1, 2, 3, 4, 5, 6, 7]
    batches = []
    async for batch_items in async_batch(items, 3):
        batches.append(batch_items)
    assert batches == [[1, 2, 3], [4, 5, 6], [7]]


