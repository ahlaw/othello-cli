import pytest

from othello.game.player import Player
from othello.game.stone import BLANK_STONE, BLACK_STONE, WHITE_STONE
from othello.game.stone import StoneFactory, StoneError


@pytest.fixture
def stone_factory():
    """Returns a StoneFactory instance."""
    return StoneFactory()


def test_blank_stone(stone_factory):
    assert stone_factory() == BLANK_STONE


def test_black_stone(stone_factory):
    assert stone_factory(Player.BLACK) == BLACK_STONE


def test_white_stone(stone_factory):
    assert stone_factory(Player.WHITE) == WHITE_STONE


def test_raises_exception_on_invalid_player_type(stone_factory):
    invalid_player = "invalid"
    with pytest.raises(StoneError):
        stone_factory(invalid_player)
