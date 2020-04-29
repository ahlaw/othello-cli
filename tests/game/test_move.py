import pytest

from othello.game.move import Move, InvalidMoveError
from othello.game.point import Point


def test_play():
    move = Move.play(Point(0, 0))
    assert move.is_play and move.point == Point(0, 0)


def test_pass_turn():
    move = Move.pass_turn()
    assert move.is_pass


def test_resign():
    move = Move.resign()
    assert move.is_resign


def test_raises_exception_on_invalid_move():
    with pytest.raises(InvalidMoveError):
        Move()
