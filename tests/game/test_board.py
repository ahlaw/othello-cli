import pytest

from othello.game.board import Board
from othello.game.board import BoardSizeError, InvalidStonePlacementError
from othello.game.player import Player
from othello.game.point import Point


@pytest.fixture
def board() -> Board:
    """Returns a Board instance with size 8."""
    return Board(8)


def test_raises_exception_below_min_board_size() -> None:
    with pytest.raises(BoardSizeError):
        Board(2)


def test_raises_exception_above_max_board_size() -> None:
    with pytest.raises(BoardSizeError):
        Board(28)


def test_raises_exception_on_odd_board_size() -> None:
    with pytest.raises(BoardSizeError):
        Board(9)


def test_correct_starting_position(board: Board) -> None:
    assert (
        board._grid[3][3] == board.stone(Player.WHITE)
        and board._grid[3][4] == board.stone(Player.BLACK)
        and board._grid[4][3] == board.stone(Player.BLACK)
        and board._grid[4][4] == board.stone(Player.WHITE)
    )


def test_get_initial_valid_moves_black(board: Board) -> None:
    valid_moves = board.get_valid_moves(Player.BLACK)
    assert valid_moves == {
        Point(3, 2): [Point(3, 3)],
        Point(2, 3): [Point(3, 3)],
        Point(5, 4): [Point(4, 4)],
        Point(4, 5): [Point(4, 4)],
    }


def test_get_initial_valid_moves_white(board: Board) -> None:
    valid_moves = board.get_valid_moves(Player.WHITE)
    assert valid_moves == {
        Point(4, 2): [Point(4, 3)],
        Point(5, 3): [Point(4, 3)],
        Point(2, 4): [Point(3, 4)],
        Point(3, 5): [Point(3, 4)],
    }


def test_get_valid_moves_custom() -> None:
    board = Board(4)
    board._grid[0][1] = board.stone(Player.WHITE)
    valid_moves = board.get_valid_moves(Player.BLACK)
    print(valid_moves)
    assert valid_moves == {
        Point(1, 0): [Point(1, 1)],
        Point(2, 3): [Point(2, 2)],
        Point(3, 2): [Point(2, 2)],
    }


def test_place_stone_valid(board: Board) -> None:
    board.place_stone(Player.BLACK, Point(2, 3))
    assert (
        board._grid[3][4] == board.stone(Player.BLACK)
        and board._grid[2][3] == board.stone(Player.BLACK)
        and board._grid[3][3] == board.stone(Player.BLACK)
        and board._grid[4][3] == board.stone(Player.BLACK)
        and board._grid[4][4] == board.stone(Player.WHITE)
    )


def test_raises_exception_on_invalid_move(board: Board) -> None:
    with pytest.raises(InvalidStonePlacementError):
        board.place_stone(Player.BLACK, Point(0, 0))


def test_count_stones_black(board: Board) -> None:
    assert board.count_stones(Player.BLACK) == 2


def test_count_stones_white(board: Board) -> None:
    assert board.count_stones(Player.WHITE) == 2


def test_board_str_size_4() -> None:
    board = Board(4)
    assert (
        str(board)
        == """ +-------+
1| | | | |
 +-------+
2| |○|●| |
 +-------+
3| |●|○| |
 +-------+
4| | | | |
 +-------+
  a b c d """
    )


def test_board_str_size_8(board: Board) -> None:
    assert (
        str(board)
        == """ +---------------+
1| | | | | | | | |
 +---------------+
2| | | | | | | | |
 +---------------+
3| | | | | | | | |
 +---------------+
4| | | |○|●| | | |
 +---------------+
5| | | |●|○| | | |
 +---------------+
6| | | | | | | | |
 +---------------+
7| | | | | | | | |
 +---------------+
8| | | | | | | | |
 +---------------+
  a b c d e f g h """
    )
