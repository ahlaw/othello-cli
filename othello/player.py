import enum

class Player(enum.Enum):
    BLACK = 1
    WHITE = 2

    @property
    def other(self):
        return Player.BLACK if self == Player.WHITE else Player.WHITE
