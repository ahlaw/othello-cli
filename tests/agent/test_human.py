"""Test cases for the human module."""
from unittest.mock import Mock

import pytest

from othello.agent.human import Human
from othello.agent.human import InvalidInputError, NotationError
from othello.game.game_state import GameState
from othello.game.move import Move
from othello.game.point import Point


@pytest.fixture
def human() -> Human:
    """Returns a Human instance."""
    return Human()


def test_valid_move(mocker: Mock, human: Human) -> None:
    """It returns a Move object on valid input."""
    mocker.patch("builtins.input", return_value="a2")
    game_state = GameState.new_game()
    assert human.select_move(game_state) == Move.play(Point(1, 0))


def test_invalid_move(mocker: Mock, human: Human) -> None:
    """It ignores invalid plays and only returns when passed a valid input."""
    mocker.patch("builtins.input", side_effect=["invalid", "a2"])
    game_state = GameState.new_game()
    assert human.select_move(game_state) == Move.play(Point(1, 0))


def test_point_to_notation(human: Human) -> None:
    """It returns notation corresponding to Point object."""
    point = Point(11, 2)
    assert Human.point_to_notation(point) == "c12"


def test_invalid_point_to_notation(human: Human) -> None:
    """It raises `NotationError` when passed an invalid Point."""
    point = Point(0, 27)
    with pytest.raises(NotationError):
        Human.point_to_notation(point)


def test_notation_to_move_pass(human: Human) -> None:
    """It returns Move object on pass."""
    assert Human.notation_to_move("pass") == Move.pass_turn()


def test_notation_to_move_resign(human: Human) -> None:
    """It returns Move object on resign."""
    assert Human.notation_to_move("resign") == Move.resign()


def test_notation_to_move_play(human: Human) -> None:
    """It returns a Move object on valid play move."""
    assert Human.notation_to_move("c12") == Move.play(Point(11, 2))


def test_valid_move_input(human: Human) -> None:
    """It returns None on valid play notation."""
    valid_input = "j25"
    assert Human.validate_input(valid_input) is None


def test_valid_pass_input(human: Human) -> None:
    """It returns None on valid pass notation."""
    valid_input = "pass"
    assert Human.validate_input(valid_input) is None


def test_valid_resign_input(human: Human) -> None:
    """It returns None when validation succeeds."""
    valid_input = "resign"
    assert Human.validate_input(valid_input) is None


def test_invalid_input(human: Human) -> None:
    """It raises `InvalidInputError` when validation fails."""
    with pytest.raises(InvalidInputError):
        invalid_input = "invalid"
        Human.validate_input(invalid_input)


def test_input_row_too_small(human: Human) -> None:
    """It raises `InvalidInputError` on notation out of range."""
    with pytest.raises(InvalidInputError):
        invalid_input = "a0"
        Human.validate_input(invalid_input)


def test_input_row_too_large(human: Human) -> None:
    """It raises `InvalidInputError` on notation out of range."""
    with pytest.raises(InvalidInputError):
        invalid_input = "a27"
        Human.validate_input(invalid_input)
