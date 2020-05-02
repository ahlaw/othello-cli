"""Player module."""
from __future__ import annotations

import enum


class Player(enum.Enum):
    """Player class representing a playable color."""

    BLACK: int = 1
    WHITE: int = 2

    @property
    def other(self) -> Player:
        """Returns the other player color.

        Returns:
            Player instance of opposite color.
        """
        return Player.BLACK if self == Player.WHITE else Player.WHITE
