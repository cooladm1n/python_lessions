from tasks import compose, partial_apply, pipe


def test_compose():
    def add_one(x):
        return x + 1

    def multiply_two(x):
        return x * 2

    composed = compose(add_one, multiply_two)
    assert composed(5) == 11  # (5 * 2) + 1


def test_partial_apply():
    def multiply(x, y, z):
        return x * y * z

    partial = partial_apply(multiply, 2, 3)
    assert partial(4) == 24  # 2 * 3 * 4


def test_pipe():
    def add_one(x):
        return x + 1

    def multiply_two(x):
        return x * 2

    def square(x):
        return x ** 2

    pipeline = pipe(add_one, multiply_two, square)
    assert pipeline(3) == 64  # ((3 + 1) * 2) ** 2


