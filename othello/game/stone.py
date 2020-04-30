from typing import Optional

from .player import Player


BLANK_STONE: str = "0"
BLACK_STONE: str = "1"
WHITE_STONE: str = "2"


class StoneError(Exception):
    pass


class Stone(str):
    __slots__ = ()


class StoneFactory:
    """
    StoneFactory class instantiates a StoneFactory object
    that can create Stone objects corresponding to either
    a player or an empty tile.
    """

    def __call__(self, player: Optional[Player] = None) -> Stone:
        if not player:
            return Stone(BLANK_STONE)
        elif player == Player.BLACK:
            return Stone(BLACK_STONE)
        elif player == Player.WHITE:
            return Stone(WHITE_STONE)
        else:
            raise StoneError("Invalid player/color for stone!")
