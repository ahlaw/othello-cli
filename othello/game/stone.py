from typing import Optional

from othello.game.player import Player


BLANK_STONE: str = " "
BLACK_STONE: str = "●"
WHITE_STONE: str = "○"


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
        if player == Player.BLACK:
            return Stone(BLACK_STONE)
        elif player == Player.WHITE:
            return Stone(WHITE_STONE)
        else:
            return Stone(BLANK_STONE)
