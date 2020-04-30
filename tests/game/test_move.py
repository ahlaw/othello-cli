import pytest

from othello.game.move import InvalidMoveError, Move
from othello.game.point import Point


def test_play() -> None:
    move = Move.play(Point(0, 0))
    assert move.is_play and move.point == Point(0, 0)


def test_pass_turn() -> None:
    move = Move.pass_turn()
    assert move.is_pass


def test_resign() -> None:
    move = Move.resign()
    assert move.is_resign


def test_raises_exception_on_invalid_move() -> None:
    with pytest.raises(InvalidMoveError):
        Move()
