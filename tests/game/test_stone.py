"""Test cases for the stone module."""
import pytest

from othello.game.player import Player
from othello.game.stone import StoneFactory


@pytest.fixture
def stone_factory() -> StoneFactory:
    """Returns a StoneFactory instance."""
    return StoneFactory()


def test_factory_blank_stone(stone_factory: StoneFactory) -> None:
    """It returns a blank character with no arguments."""
    assert stone_factory() == " "


def test_factory_black_stone(stone_factory: StoneFactory) -> None:
    """It returns a black circle when passed black player."""
    assert stone_factory(Player.BLACK) == "○"


def test_factory_white_stone(stone_factory: StoneFactory) -> None:
    """It returns a black circle when passed white player."""
    assert stone_factory(Player.WHITE) == "●"
