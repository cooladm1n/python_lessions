# Lesson 07: Dates and Time

Estimated time: 45-75 minutes

Learning outcomes
- Parse and format dates using `datetime` and `dateutil` (optional).
- Compute differences between dates and handle timezones basics.

Acceptance criteria
- Implement `parse_date(s: str) -> datetime.date` for `YYYY-MM-DD`.
- Implement `days_between(d1: date, d2: date) -> int` returning absolute days.

Worked example

```py
from datetime import datetime, date

def parse_date(s: str) -> date:
	return datetime.strptime(s, "%Y-%m-%d").date()

def days_between(d1: date, d2: date) -> int:
	return abs((d2 - d1).days)
```

Exercises (mandatory)
1) Implement `parse_date` and `days_between` and test for correctness.
2) Implement `format_timestamp(dt)` returning ISO 8601 string with timezone info when available.

Hints & testing
- Test with leap-year dates and end-of-month boundaries.
- For timezone-aware tasks, recommend using `pytz` or `zoneinfo` (Python 3.9+).


