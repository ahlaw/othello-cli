from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .point import Point


class InvalidMoveError(Exception):
    """
    Exception class for invalid Move object initialization.
    """

    pass


@dataclass
class Move:
    """
    Move class representing a chosen move. Should be
    instantiated with one of the defined alternative
    constructors.
    """

    point: Optional[Point] = None
    is_pass: bool = False
    is_resign: bool = False

    def __post_init__(self) -> None:
        self.is_play = self.point is not None
        if not (self.is_play ^ self.is_pass ^ self.is_resign):
            raise InvalidMoveError("Invalid instantiation of Move object!")

    @classmethod
    def play(cls, point: Point) -> Move:
        return Move(point=point)

    @classmethod
    def pass_turn(cls) -> Move:
        return Move(is_pass=True)

    @classmethod
    def resign(cls) -> Move:
        return Move(is_resign=True)
