import pytest

from othello.move import Move, InvalidMoveError
from othello.point import Point


def test_play():
    move = Move(point=Point(0, 0))
    assert move.is_play and move.point == Point(0, 0)

def test_pass_turn():
    move = Move(is_pass=True)
    assert move.is_pass

def test_resign():
    move = Move(is_resign=True)
    assert move.is_resign

def test_raises_exception_on_invalid_move():
    with pytest.raises(InvalidMoveError):
        Move()
