# Lesson 11: Asyncio and Concurrency Basics

Estimated time: 60-90 minutes

Learning outcomes
- Understand `async`/`await`, tasks, and the event loop.
- Run coroutines concurrently (gather) and control concurrency (Semaphore).
- Offload blocking work using `to_thread`.
- Build a simple producer/consumer pipeline with `asyncio.Queue`.

Acceptance criteria
- `fetch(name, delay)` returns a string including the name and indicates completion.
- `run_three()` launches three `fetch` coroutines and returns their results as a list of strings (len == 3).
- `offload_square(x)` uses `to_thread` (or equivalent) to compute x*x without blocking the event loop.

Exercises (mandatory)
1) Implement `fetch(name: str, delay: float) -> str` that awaits `asyncio.sleep(delay)` and returns a message like "{name} done after {delay}".
2) Implement `run_three()` to run 3 `fetch` coroutines concurrently and return their results.
3) Implement `offload_square(x)` which offloads integer squaring to a thread and returns the result.

Optional (stretch)
- Implement a Semaphore-limited pool that fetches many names but only N concurrently.
- Build a producer-consumer pipeline using `asyncio.Queue` and measure throughput.

Testing notes
- Use `pytest` and `asyncio.run` (or pytest-asyncio fixtures) for async tests.
- Avoid brittle timing assertions; prefer checking structure and expected substrings.
