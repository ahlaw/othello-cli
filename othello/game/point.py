"""Point module."""
from typing import NamedTuple


class Point(NamedTuple):
    """Point on board."""

    row: int
    col: int
