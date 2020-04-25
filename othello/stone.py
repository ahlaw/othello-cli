from .player import Player


BLANK_STONE = '0'
BLACK_STONE = '1'
WHITE_STONE = '2'


class StoneError(Exception):
    pass


class Stone(str):
    __slots__ = ()


class StoneFactory:
    def __call__(self, player=None):
        if not player:
            return Stone(BLANK_STONE)
        elif player == Player.BLACK:
            return Stone(BLACK_STONE)
        elif player == Player.WHITE:
            return Stone(WHITE_STONE)
        else:
            raise StoneError('Invalid player/color for stone!')
