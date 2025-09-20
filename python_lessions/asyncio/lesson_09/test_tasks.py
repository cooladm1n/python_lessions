import asyncio
import pytest
from tasks import AsyncMock, AsyncTestRunner, AsyncFixture


async def test_async_mock():
    mock = AsyncMock(return_value="test_result")
    
    result = await mock("arg1", "arg2")
    assert result == "test_result"
    assert mock.call_count == 1
    assert mock.call_args_list[0] == (("arg1", "arg2"), {})
    
    mock.assert_called_once_with("arg1", "arg2")


async def test_async_test_runner():
    runner = AsyncTestRunner()
    
    async def test_1():
        return "test_1_passed"
    
    async def test_2():
        return "test_2_passed"
    
    runner.add_test(test_1)
    runner.add_test(test_2)
    
    results = await runner.run_tests()
    assert len(results) == 2
    assert any("test_1_passed" in str(result) for result in results)


async def test_async_fixture():
    async def setup():
        return "fixture_value"
    
    async def teardown():
        pass
    
    async with AsyncFixture(setup, teardown) as fixture:
        assert fixture == "fixture_value"


