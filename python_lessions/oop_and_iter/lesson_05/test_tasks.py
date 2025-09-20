from tasks import Vector, BankAccount, Counter


def test_vector():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3.x == 4 and v3.y == 6
    v4 = v1 * 2
    assert v4.x == 2 and v4.y == 4
    assert str(v1) == "Vector(1, 2)"


def test_bank_account():
    acc1 = BankAccount(100)
    acc2 = BankAccount(100)
    acc3 = BankAccount(200)
    assert acc1 == acc2
    assert acc1 < acc3


def test_counter():
    c = Counter()
    c["apples"] = 5
    c["oranges"] = 3
    assert len(c) == 2
    assert c["apples"] == 5
    assert c["missing"] == 0


