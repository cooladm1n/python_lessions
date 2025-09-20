# Lesson 11: Asyncio and Concurrency Basics

In this lesson you will learn:
- `async`/`await` syntax and the event loop
- Running coroutines concurrently with `gather`
- Async-friendly primitives: `sleep`, `Semaphore`, `Queue`
- Offloading CPU-bound/blocking tasks with `to_thread`
- Pitfalls: blocking calls in async code, ensuring cancellation/finalization

Exercises:
1) Implement `async fetch(url)` that simulates network latency.
2) Launch 3 tasks concurrently and measure total time.
3) Convert a blocking function to run in a thread with `to_thread`.
4) Limit concurrency with a `Semaphore` and collect results.
5) Build a small producer-consumer pipeline using an `asyncio.Queue`.
