"""Test cases for the board module."""
import pytest

from othello.game.board import Board
from othello.game.board import BoardSizeError, InvalidDiscPlacementError
from othello.game.player import Player
from othello.game.point import Point


@pytest.fixture
def board() -> Board:
    """Returns a Board instance with size 8."""
    return Board(8)


def test_board_size_below_min() -> None:
    """It raises `BoardSizeError` when size is below minimum."""
    with pytest.raises(BoardSizeError):
        Board(2)


def test_board_size_above_max() -> None:
    """It raises `BoardSizeError` when size is above maximum."""
    with pytest.raises(BoardSizeError):
        Board(28)


def test_odd_board_size() -> None:
    """It raises `BoardSizeError` when size is odd."""
    with pytest.raises(BoardSizeError):
        Board(9)


def test_initial_valid_moves_black(board: Board) -> None:
    """It returns black valid moves in the initial game state."""
    valid_moves = board.get_valid_moves(Player.BLACK)
    assert valid_moves == {
        Point(3, 2): [Point(3, 3)],
        Point(2, 3): [Point(3, 3)],
        Point(5, 4): [Point(4, 4)],
        Point(4, 5): [Point(4, 4)],
    }


def test_initial_valid_moves_white(board: Board) -> None:
    """It returns white valid moves in the initial game state."""
    valid_moves = board.get_valid_moves(Player.WHITE)
    assert valid_moves == {
        Point(4, 2): [Point(4, 3)],
        Point(5, 3): [Point(4, 3)],
        Point(2, 4): [Point(3, 4)],
        Point(3, 5): [Point(3, 4)],
    }


def test_valid_disc_placement(board: Board) -> None:
    """It returns white valid moves after black's first move."""
    board.place_disc(Player.BLACK, Point(2, 3))
    valid_moves = board.get_valid_moves(Player.WHITE)
    assert valid_moves == {
        Point(2, 2): [Point(3, 3)],
        Point(2, 4): [Point(3, 4)],
        Point(4, 2): [Point(4, 3)],
    }


def test_invalid_disc_placement(board: Board) -> None:
    """It raises `InvalidDiscPlacementError` on invalid move for place_disc."""
    with pytest.raises(InvalidDiscPlacementError):
        board.place_disc(Player.BLACK, Point(0, 0))


def test_count_discs_black(board: Board) -> None:
    """It counts the number of black discs on board."""
    assert board.count_discs(Player.BLACK) == 2


def test_count_discs_white(board: Board) -> None:
    """It counts the number of white discs on board."""
    assert board.count_discs(Player.WHITE) == 2


def test_board_str_size_4() -> None:
    """It returns the str representation for size 4 Board."""
    board = Board(4)
    assert (
        str(board)
        == """ +-------+
1| | | | |
 +-------+
2| |●|○| |
 +-------+
3| |○|●| |
 +-------+
4| | | | |
 +-------+
  a b c d """
    )


def test_board_str_size_8(board: Board) -> None:
    """It returns the str representation for size 8 Board."""
    assert (
        str(board)
        == """ +---------------+
1| | | | | | | | |
 +---------------+
2| | | | | | | | |
 +---------------+
3| | | | | | | | |
 +---------------+
4| | | |●|○| | | |
 +---------------+
5| | | |○|●| | | |
 +---------------+
6| | | | | | | | |
 +---------------+
7| | | | | | | | |
 +---------------+
8| | | | | | | | |
 +---------------+
  a b c d e f g h """
    )
