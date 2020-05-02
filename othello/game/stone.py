"""Stone module."""
from typing import Optional

from othello.game.player import Player


BLANK_STONE: str = " "
BLACK_STONE: str = "○"
WHITE_STONE: str = "●"


class Stone(str):
    """Stone object."""

    __slots__ = ()


class StoneFactory:
    """Creates Stone objects."""

    def __call__(self, player: Optional[Player] = None) -> Stone:
        """Returns Stone object based on given player.

        Returns the Stone object corresponding to the player color
        if a Player type is passed, or a blank Stone if no argument
        is passed.

        Args:
            player: Stone will be made for this player (blank stone if None).

        Returns:
            Corresponding Stone object.
        """
        if player == Player.BLACK:
            return Stone(BLACK_STONE)
        elif player == Player.WHITE:
            return Stone(WHITE_STONE)
        else:
            return Stone(BLANK_STONE)
