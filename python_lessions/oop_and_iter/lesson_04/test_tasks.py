import pytest
from tasks import Temperature, Rectangle, Person


def test_temperature():
    t = Temperature(25.0)
    assert t.celsius == 25.0
    t.celsius = 30.0
    assert t.celsius == 30.0
    with pytest.raises(ValueError):
        t.celsius = -300.0


def test_rectangle():
    r = Rectangle(5.0, 3.0)
    assert r.area == 15.0
    assert r.perimeter == 16.0


def test_person():
    p = Person("Alice", 1990)
    current_year = datetime.now().year
    expected_age = current_year - 1990
    assert p.age == expected_age
    p.age = 25
    assert p._birth_year == current_year - 25


