"""Disc module."""
from typing import Optional

from othello.game.player import Player


BLANK_DISC: str = " "
BLACK_DISC: str = "○"
WHITE_DISC: str = "●"


class Disc(str):
    """Disc object."""

    __slots__ = ()


def get_disc(player: Optional[Player] = None) -> Disc:
    """Returns Disc object based on given player.

    Returns the Disc object corresponding to the player color
    if a Player type is passed, or a blank Disc if no argument
    is passed.

    Args:
        player: Disc will be made for this player (blank disc if None).

    Returns:
        Corresponding Disc object.
    """
    if player == Player.BLACK:
        return Disc(BLACK_DISC)
    elif player == Player.WHITE:
        return Disc(WHITE_DISC)
    else:
        return Disc(BLANK_DISC)
