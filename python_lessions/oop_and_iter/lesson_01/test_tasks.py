import pytest
from tasks import BankAccount, Point


def test_bank_account():
    acct = BankAccount("Alice", 100)
    acct.deposit(50)
    assert acct.balance == 150
    acct.withdraw(25)
    assert acct.balance == 125
    with pytest.raises(ValueError):
        BankAccount("Bob", -1)
    with pytest.raises(ValueError):
        acct.withdraw(999)


def test_point_distance():
    p = Point(3, 4)
    assert p.distance_to_origin() == 5
