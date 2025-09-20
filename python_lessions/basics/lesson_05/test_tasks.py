from tasks import squares_of_evens, word_lengths, dedupe_preserve_order


def test_squares_of_evens():
    assert squares_of_evens(10) == [4, 16, 36, 64, 100]


def test_word_lengths():
    words = ["apple", "banana", "kiwi"]
    assert word_lengths(words) == {"apple": 5, "banana": 6, "kiwi": 4}


def test_dedupe_preserve_order():
    items = ["a", "b", "a", "c", "b", "d"]
    assert dedupe_preserve_order(items) == ["a", "b", "c", "d"]
