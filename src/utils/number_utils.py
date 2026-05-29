def format_currency(amount: float, symbol: str = "$") -> str:
    """Format a number as currency with thousands separators and two decimal places."""
    return f"{symbol}{amount:,.2f}"


def clamp(value: float, lo: float, hi: float) -> float:
    """Restrict value to the inclusive range [lo, hi]."""
    return max(lo, min(hi, value))
