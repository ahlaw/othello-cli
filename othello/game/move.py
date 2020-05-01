from __future__ import annotations

from typing import Any, Optional

from .point import Point


class InvalidMoveError(Exception):
    """
    Exception class for invalid Move object initialization.
    """

    pass


class Move:
    """
    Move class representing a chosen move. Should be
    instantiated with one of the defined alternative
    constructors.
    """

    def __init__(
        self,
        point: Optional[Point] = None,
        is_pass: bool = False,
        is_resign: bool = False,
    ) -> None:
        if not ((point is not None) ^ is_pass ^ is_resign):
            raise InvalidMoveError("Invalid instantiation of Move object!")
        self.point = point
        self.is_play = self.point is not None
        self.is_pass = is_pass
        self.is_resign = is_resign

    def __eq__(self, other: Any) -> bool:
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (
            self.point == other.point
            and self.is_play == other.is_play
            and self.is_pass == other.is_pass
            and self.is_resign == other.is_resign
        )

    @classmethod
    def play(cls, point: Point) -> Move:
        return Move(point=point)

    @classmethod
    def pass_turn(cls) -> Move:
        return Move(is_pass=True)

    @classmethod
    def resign(cls) -> Move:
        return Move(is_resign=True)
