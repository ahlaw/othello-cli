"""Test cases for the random_bot module."""
from unittest.mock import Mock

import pytest

from othello.agent.random_bot import RandomBot
from othello.game.game_state import GameState
from othello.game.move import Move
from othello.game.point import Point


@pytest.fixture
def random_bot() -> RandomBot:
    """Returns a RandomBot instance."""
    return RandomBot()


def test_plays_random_move(mocker: Mock, random_bot: RandomBot) -> None:
    """It returns a random Move from legal moves."""
    mocker.patch("random.choice", lambda n: n[0])
    mocker.patch.object(
        GameState, "legal_moves", return_value=[Point(0, 0), Point(1, 1)]
    )
    game_state = GameState.new_game()
    selected = random_bot.select_move(game_state)
    assert selected == Move.play(Point(0, 0))


def test_pass_when_no_plays(mocker: Mock, random_bot: RandomBot) -> None:
    """It returns a pass Move when there are no legal moves."""
    mocker.patch.object(GameState, "legal_moves", return_value=[])
    game_state = GameState.new_game()
    selected = random_bot.select_move(game_state)
    assert selected == Move.pass_turn()
