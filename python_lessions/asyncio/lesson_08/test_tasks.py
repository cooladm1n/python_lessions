import asyncio
from unittest.mock import AsyncMock, patch
from tasks import AsyncDatabase, AsyncTransaction, AsyncQueryBuilder


async def test_async_database():
    with patch('aiosqlite.connect') as mock_connect:
        mock_connection = AsyncMock()
        mock_cursor = AsyncMock()
        mock_cursor.fetchall.return_value = [{"id": 1, "name": "Alice"}]
        mock_connection.execute.return_value = mock_cursor
        mock_connect.return_value.__aenter__.return_value = mock_connection
        
        async with AsyncDatabase("sqlite:///:memory:") as db:
            result = await db.execute("SELECT * FROM users")
            assert result == [{"id": 1, "name": "Alice"}]


async def test_async_transaction():
    with patch('aiosqlite.connect') as mock_connect:
        mock_connection = AsyncMock()
        mock_cursor = AsyncMock()
        mock_cursor.fetchall.return_value = [{"id": 1}]
        mock_connection.execute.return_value = mock_cursor
        mock_connect.return_value.__aenter__.return_value = mock_connection
        
        async with AsyncDatabase("sqlite:///:memory:") as db:
            async with AsyncTransaction(db) as tx:
                result = await tx.execute("INSERT INTO users (name) VALUES (?)", {"name": "Alice"})
                assert result == [{"id": 1}]


def test_async_query_builder():
    builder = AsyncQueryBuilder()
    query, params = builder.select(["id", "name"]).from_table("users").where("age > ?", 18).build()
    
    assert "SELECT id, name FROM users WHERE age > ?" in query
    assert params["age"] == 18


