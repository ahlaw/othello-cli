"""Test cases for the move module."""
import pytest

from othello.game.move import InvalidMoveError, Move
from othello.game.point import Point


def test_play() -> None:
    """It returns play Move object with correct fields."""
    move = Move.play(Point(0, 0))
    assert move.is_play and move.point == Point(0, 0)


def test_pass_turn() -> None:
    """It returns pass Move object with correct fields."""
    move = Move.pass_turn()
    assert move.is_pass


def test_resign() -> None:
    """It returns resign Move object with correct fields."""
    move = Move.resign()
    assert move.is_resign


def test_invalid_move() -> None:
    """It raises `InvalidMoveError` on invalid Move initialization."""
    with pytest.raises(InvalidMoveError):
        Move()


def test_equality_play() -> None:
    """It declares two play Move objects with same fields as equal."""
    assert Move.play(Point(0, 0)) == Move.play(Point(0, 0))


def test_equality_pass() -> None:
    """It declares two pass Move objects with same fields as equal."""
    assert Move.pass_turn() == Move.pass_turn()


def test_equality_resign() -> None:
    """It declares two resign Move objects with same fields as equal."""
    assert Move.resign() == Move.resign()
