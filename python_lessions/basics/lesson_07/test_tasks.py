from datetime import date, datetime
from tasks import parse_date, days_between, format_timestamp


def test_parse_date():
    assert parse_date("2023-12-25") == date(2023, 12, 25)


def test_days_between():
    d1 = date(2023, 1, 1)
    d2 = date(2023, 1, 10)
    assert days_between(d1, d2) == 9
    assert days_between(d2, d1) == 9


def test_format_timestamp():
    dt = datetime(2023, 12, 25, 15, 30, 45)
    result = format_timestamp(dt)
    assert "2023-12-25T15:30:45" in result


