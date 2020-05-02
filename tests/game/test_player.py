"""Test cases for the player module."""
from othello.game.player import Player


def test_other_player_from_white() -> None:
    """It returns the other player from white is black."""
    assert Player.WHITE.other == Player.BLACK


def test_other_player_from_black() -> None:
    """It returns the other player from black is white."""
    assert Player.BLACK.other == Player.WHITE
