from tasks import Range, fibonacci, batch


def test_range():
    r = Range(1, 5)
    numbers = list(r)
    assert numbers == [1, 2, 3, 4]


def test_fibonacci():
    fib = fibonacci()
    first_ten = [next(fib) for _ in range(10)]
    assert first_ten == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_batch():
    items = [1, 2, 3, 4, 5, 6, 7]
    batches = list(batch(items, 3))
    assert batches == [[1, 2, 3], [4, 5, 6], [7]]


