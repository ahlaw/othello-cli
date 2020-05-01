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


def test_select_valid_move(mocker: Mock, human: Human) -> None:
    mocker.patch("builtins.input", return_value="a2")
    game_state = GameState.new_game()
    assert human.select_move(game_state) == Move.play(Point(1, 0))


def test_select_ignore_invalid_move(mocker: Mock, human: Human) -> None:
    mocker.patch("builtins.input", side_effect=["invalid", "a2"])
    game_state = GameState.new_game()
    assert human.select_move(game_state) == Move.play(Point(1, 0))


def test_point_to_notation(human: Human) -> None:
    point = Point(11, 2)
    assert Human.point_to_notation(point) == "c12"


def test_raises_error_on_invalid_point_to_notation(human: Human) -> None:
    point = Point(0, 27)
    with pytest.raises(NotationError):
        Human.point_to_notation(point)


def test_notation_to_move_pass(human: Human) -> None:
    assert Human.notation_to_move("pass") == Move.pass_turn()


def test_notation_to_move_resign(human: Human) -> None:
    assert Human.notation_to_move("resign") == Move.resign()


def test_notation_to_move_play(human: Human) -> None:
    assert Human.notation_to_move("c12") == Move.play(Point(11, 2))


def test_do_not_raise_exception_on_valid_move_input(human: Human) -> None:
    valid_input = "j25"
    assert Human.validate_input(valid_input) is None


def test_do_not_raise_exception_on_valid_pass_input(human: Human) -> None:
    valid_input = "pass"
    assert Human.validate_input(valid_input) is None


def test_do_not_raise_exception_on_valid_resign_input(human: Human) -> None:
    valid_input = "resign"
    assert Human.validate_input(valid_input) is None


def test_raises_exception_on_invalid_input(human: Human) -> None:
    with pytest.raises(InvalidInputError):
        invalid_input = "invalid"
        Human.validate_input(invalid_input)


def test_raises_exception_on_input_row_too_small(human: Human) -> None:
    with pytest.raises(InvalidInputError):
        invalid_input = "a0"
        Human.validate_input(invalid_input)


def test_raises_exception_on_input_row_too_large(human: Human) -> None:
    with pytest.raises(InvalidInputError):
        invalid_input = "a27"
        Human.validate_input(invalid_input)
