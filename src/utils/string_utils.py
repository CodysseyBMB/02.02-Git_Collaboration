"""Text utility functions."""

import re
import unicodedata


def slugify(text: str) -> str:
    """Convert text to a lowercase hyphenated slug.

    Non-ASCII letters are normalized to ASCII where possible, then
    characters that are not alphanumeric or whitespace are removed.
    """
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = ascii_text.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", lowered)
    slug = re.sub(r"[\s_-]+", "-", slug)
    return slug.strip("-")


def truncate(text: str, max_len: int) -> str:
    """Return text truncated to max_len, with '...' if shortened."""
    if max_len < 0:
        raise ValueError("max_len must be non-negative")
    if len(text) <= max_len:
        return text
    if max_len <= 3:
        return "." * max_len
    return text[: max_len - 3] + "..."


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words."""
    if not text or not text.strip():
        return 0
    return len(text.split())
