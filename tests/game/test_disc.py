"""Test cases for the disc module."""
from othello.game.disc import get_disc
from othello.game.player import Player


def test_get_blank_disc() -> None:
    """It returns a blank character with no arguments."""
    assert get_disc() == " "


def test_get_black_disc() -> None:
    """It returns a black circle when passed black player."""
    assert get_disc(Player.BLACK) == "○"


def test_get_white_disc() -> None:
    """It returns a black circle when passed white player."""
    assert get_disc(Player.WHITE) == "●"
