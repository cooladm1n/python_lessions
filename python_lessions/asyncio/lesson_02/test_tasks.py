import asyncio
from pathlib import Path
from tasks import AsyncFile, AsyncDatabase, AsyncLock


async def test_async_file(tmp_path: Path):
    file_path = tmp_path / "test.txt"
    async with AsyncFile(file_path, "w") as f:
        await f.write("hello world")
    
    async with AsyncFile(file_path, "r") as f:
        content = await f.read()
        assert content == "hello world"


async def test_async_database():
    async with AsyncDatabase("sqlite:///:memory:") as db:
        result = await db.execute("SELECT 1")
        assert result == [1]


async def test_async_lock():
    lock = AsyncLock()
    async with lock:
        assert lock._locked is True
    assert lock._locked is False


