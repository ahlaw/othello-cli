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

    def __init__(self, point=None, is_pass=False, is_resign=False):
        if not ((point is not None) ^ is_pass ^ is_resign):
            raise InvalidMoveError("Invalid instantiation of Move object!")
        self.point = point
        self.is_play = self.point is not None
        self.is_pass = is_pass
        self.is_resign = is_resign

    @classmethod
    def play(cls, point):
        return Move(point=point)

    @classmethod
    def pass_turn(cls):
        return Move(is_pass=True)

    @classmethod
    def resign(cls):
        return Move(is_resign=True)
