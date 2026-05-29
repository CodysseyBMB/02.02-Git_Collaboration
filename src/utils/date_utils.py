"""Date utility helpers owned by team member 2."""

from datetime import date, datetime


def days_between(a: date, b: date) -> int:
    """Return the absolute number of days between two dates.

    Example:
        days_between(date(2026, 5, 1), date(2026, 5, 29)) -> 28
    """
    return abs((b - a).days)


def to_iso(d: date) -> str:
    """Return a date as a YYYY-MM-DD string.

    Example:
        to_iso(date(2026, 5, 29)) -> "2026-05-29"
    """
    if isinstance(d, datetime):
        d = d.date()
    return d.isoformat()


__all__ = ["days_between", "to_iso"]
