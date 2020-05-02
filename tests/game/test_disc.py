"""Test cases for the disc module."""
import pytest

from othello.game.disc import DiscFactory
from othello.game.player import Player


@pytest.fixture
def disc_factory() -> DiscFactory:
    """Returns a DiscFactory instance."""
    return DiscFactory()


def test_factory_blank_disc(disc_factory: DiscFactory) -> None:
    """It returns a blank character with no arguments."""
    assert disc_factory() == " "


def test_factory_black_disc(disc_factory: DiscFactory) -> None:
    """It returns a black circle when passed black player."""
    assert disc_factory(Player.BLACK) == "○"


def test_factory_white_disc(disc_factory: DiscFactory) -> None:
    """It returns a black circle when passed white player."""
    assert disc_factory(Player.WHITE) == "●"
