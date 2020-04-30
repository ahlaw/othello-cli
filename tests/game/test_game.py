import pytest

from othello.game.game_state import GameState, InvalidMoveError
from othello.game.move import Move
from othello.game.player import Player
from othello.game.point import Point


@pytest.fixture
def new_game() -> GameState:
    """Returns a new Game instance."""
    return GameState.new_game()


def test_apply_move_play(new_game: GameState) -> None:
    game = new_game.apply_move(Move.play(Point(3, 2)))
    assert (
        game.current_player == Player.WHITE
        and game.board != new_game.board
        and game.last_move.is_play
    )


def test_apply_move_resign(new_game: GameState) -> None:
    game = new_game.apply_move(Move.resign())
    assert (
        game.current_player == Player.WHITE
        and game.board == new_game.board
        and game.last_move.is_resign
    )


def test_legal_moves(new_game: GameState) -> None:
    legal_moves = new_game.legal_moves()
    assert sorted(legal_moves) == [Point(2, 3), Point(3, 2), Point(4, 5), Point(5, 4)]


def test_raises_exception_on_illegal_stone_placement(new_game: GameState) -> None:
    with pytest.raises(InvalidMoveError):
        new_game.apply_move(Move.play(Point(0, 0)))


def test_raises_exception_on_illegal_pass(new_game: GameState) -> None:
    with pytest.raises(InvalidMoveError):
        new_game.apply_move(Move.pass_turn())


def test_game_not_over_at_start(new_game: GameState) -> None:
    assert not new_game.is_over()


def test_game_not_over_after_move(new_game: GameState) -> None:
    game = new_game.apply_move(Move.play(Point(3, 2)))
    assert not game.is_over()


def test_game_over_after_resign(new_game: GameState) -> None:
    game = new_game.apply_move(Move.resign())
    assert game.is_over()


def test_game_over_after_two_passes() -> None:
    game = GameState.new_game(board_size=4)
    moves = [
        Point(1, 0),
        Point(0, 0),
        Point(0, 1),
        Point(0, 2),
        Point(1, 3),
        Point(2, 0),
        Point(3, 0),
        Point(3, 2),
        Point(3, 1),
        Point(0, 3),
        Point(3, 3),
        Point(2, 3),
    ]
    for point in moves:
        game = game.apply_move(Move.play(point))
    game = game.apply_move(Move.pass_turn())
    game = game.apply_move(Move.pass_turn())
    assert game.is_over()


def test_white_wins_when_black_resigns(new_game: GameState) -> None:
    game = new_game.apply_move(Move.resign())
    assert game.winner() == Player.WHITE


def test_black_wins_with_more_stones(new_game: GameState) -> None:
    game = new_game.apply_move(Move.play(Point(3, 2)))
    assert game.winner() == Player.BLACK


def test_white_wins_with_more_stones(new_game: GameState) -> None:
    game = new_game.apply_move(Move.play(Point(3, 2)))
    game = game.apply_move(Move.play(Point(2, 2)))
    game = game.apply_move(Move.play(Point(2, 3)))
    game = game.apply_move(Move.play(Point(4, 2)))
    assert game.winner() == Player.WHITE


def test_game_draw(new_game: GameState) -> None:
    assert new_game.winner() is None
