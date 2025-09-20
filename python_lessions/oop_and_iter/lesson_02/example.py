"""
Lesson 10: Generators and Context Managers
"""
from contextlib import contextmanager
from time import perf_counter
from itertools import islice, count, chain, groupby


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

@contextmanager
def timer(label: str):
    start = perf_counter()
    try:
        yield
    finally:
        duration = perf_counter() - start
        print(f"{label}: {duration:.6f}s")

with timer("first 10 fibs"):
    g = fib()
    first_ten = list(islice(g, 10))
print(first_ten)

# Generator expression and chain
a = (x * x for x in range(5))
b = (x + 10 for x in range(5))
print(list(chain(a, b)))

# Groupby example: group words by first letter
words = ["apple", "apricot", "banana", "blueberry", "cherry"]
words_sorted = sorted(words, key=lambda w: w[0])
for key, group in groupby(words_sorted, key=lambda w: w[0]):
    print(key, list(group))

# islice on infinite counter
print(list(islice(count(start=100, step=7), 5)))
