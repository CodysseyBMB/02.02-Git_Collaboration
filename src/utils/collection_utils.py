"""Collection utility helpers owned by team member 2."""

from collections.abc import Hashable, Iterable
from typing import TypeVar

T = TypeVar("T")


def chunk(items: list[T], size: int) -> list[list[T]]:
    """Split items into lists of the given size.

    Example:
        chunk([1, 2, 3, 4, 5], 2) -> [[1, 2], [3, 4], [5]]
    """
    if size <= 0:
        raise ValueError("size must be greater than 0")
    return [items[index : index + size] for index in range(0, len(items), size)]


def unique(items: Iterable[T]) -> list[T]:
    """Return unique items while preserving their original order.

    Example:
        unique(["a", "b", "a"]) -> ["a", "b"]
    """
    seen_hashable: set[Hashable] = set()
    seen_unhashable: list[T] = []
    result: list[T] = []

    for item in items:
        if isinstance(item, Hashable):
            if item in seen_hashable:
                continue
            seen_hashable.add(item)
        else:
            if item in seen_unhashable:
                continue
            seen_unhashable.append(item)
        result.append(item)

    return result


__all__ = ["chunk", "unique"]
