"""Move module."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from othello.game.point import Point


class InvalidMoveError(Exception):
    """Raised upon invalid Move object initialization."""

    pass


@dataclass
class Move:
    """Represents a player's move.

    Should be instantiated with one of the defined alternative
    constructors.

    Attributes:
        point: Point to play if move is play, otherwise None.
        is_play: A boolean indicating if the move is play disc.
        is_pass: A boolean indicating if the move is pass.
        is_resign: A boolean indicating if the move is resign.
    """

    point: Optional[Point] = None
    is_pass: bool = False
    is_resign: bool = False

    def __post_init__(self) -> None:
        """Post initialization.

        Sets the is_play attribute if point attribute was initialized.
        Then checks if only of the boolean attributes was set.

        Raises:
            InvalidMoveError: If more than one boolean attribute was set
        """
        self.is_play = self.point is not None
        if not (self.is_play ^ self.is_pass ^ self.is_resign):
            raise InvalidMoveError("Invalid instantiation of Move object!")

    @classmethod
    def play(cls, point: Point) -> Move:
        """Constructor for play type Move.

        Args:
            point: A Point representing where to play.

        Returns:
            A play type Move instance.
        """
        return Move(point=point)

    @classmethod
    def pass_turn(cls) -> Move:
        """Constructor for pass type Move.

        Returns:
            A pass type Move instance.
        """
        return Move(is_pass=True)

    @classmethod
    def resign(cls) -> Move:
        """Constructor for resign type Move.

        Returns:
            A resign type Move instance.
        """
        return Move(is_resign=True)
