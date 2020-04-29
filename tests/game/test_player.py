from othello.game.player import Player


def test_other_player_from_white_returns_black():
    assert Player.WHITE.other == Player.BLACK


def test_other_player_from_black_returns_white():
    assert Player.BLACK.other == Player.WHITE
