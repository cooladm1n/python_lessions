import asyncio
from tasks import fetch, run_three, offload_square


def test_fetch_event_loop():
    result = asyncio.run(fetch("X", 0.01))
    assert result.startswith("X done after")


def test_run_three():
    results = asyncio.run(run_three())
    assert len(results) == 3


def test_offload_square():
    val = asyncio.run(offload_square(7))
    assert val == 49
