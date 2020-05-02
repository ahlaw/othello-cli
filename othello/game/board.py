"""Board module."""
import itertools
import string
from typing import Dict, List, Tuple

from othello.game import disc
from othello.game.player import Player
from othello.game.point import Point

MIN_BOARD_SIZE = 4
MAX_BOARD_SIZE = 26


class BoardSizeError(Exception):
    """Raised when initializing Board object with invalid board size."""

    pass


class InvalidDiscPlacementError(Exception):
    """Raised when placing disc on Board at an invalid location."""

    pass


class Board:
    """Othello board.

    Board instances keep track of what color discs are on what locations.

    Attributes:
        size: Board size.
    """

    def __init__(self, size: int) -> None:
        """Default constructor for Board.

        Checks if board size is valid and sets up initial disc
        positions.

        Args:
            size: Board size.

        Raises:
            BoardSizeError: Invalid board size.
        """
        if not MIN_BOARD_SIZE <= size or not MAX_BOARD_SIZE >= size or size % 2 != 0:
            raise BoardSizeError(f"{size} is invalid size!")

        self.size = size

        center = size // 2 - 1
        self._grid = [[disc.get_disc()] * size for _ in range(size)]
        self._grid[center][center] = disc.get_disc(Player.WHITE)
        self._grid[center][center + 1] = disc.get_disc(Player.BLACK)
        self._grid[center + 1][center] = disc.get_disc(Player.BLACK)
        self._grid[center + 1][center + 1] = disc.get_disc(Player.WHITE)

    def __str__(self) -> str:
        """ASCII graphical representation of Board.

        Returns:
            String representation.
        """
        rowline = f" +{'-' * (self.size * 2 - 1)}+"
        rowlines = [rowline] * (self.size + 1)

        rows = [f"{i+1}|{'|'.join(row)}|" for i, row in enumerate(self._grid)]
        columns = string.ascii_lowercase[: self.size]
        rows.append(f"  {' '.join(columns)} ")

        return "\n".join(itertools.chain(*zip(rowlines, rows)))

    def count_discs(self, player: Player) -> int:
        """Count discs on board corresponding to the given player.

        Args:
            player: Player whose discs are counted.

        Returns:
            Disc count.
        """
        count = 0
        player_disc = disc.get_disc(player)
        for i in range(self.size):
            for j in range(self.size):
                if self._grid[i][j] == player_disc:
                    count += 1
        return count

    def place_disc(self, player: Player, point: Point) -> None:
        """Place disc corresponding to player at the given point.

        If the move is valid, the Board instance will be updated to
        reflect the disc being at that point and all outflanked discs
        being reversed.

        Args:
            player: The disc placed corresponds to this player.
            point: The disc will be placed at this point.

        Raises:
            InvalidDiscPlacementError: If disc cannot legally be placed
                at the given point.
        """
        valid_moves = self.get_valid_moves(player)

        if point not in valid_moves:
            raise InvalidDiscPlacementError(f"{point} is not a valid move!")

        self._grid[point.row][point.col] = disc.get_disc(player)
        outflanks = valid_moves[point]
        for row, col in outflanks:
            self._grid[row][col] = disc.get_disc(player)

    def get_valid_moves(self, player: Player) -> Dict[Point, List[Point]]:
        """Get valid moves and their captures.

        Args:
            player: Player whose moves are considered.

        Returns:
            Dictionary mapping valid disc placements to discs captured by the
            move.
        """
        valid_moves = {}
        for row in range(self.size):
            for col in range(self.size):
                point = Point(row, col)
                outflanks = self._get_outflanks(player, point)
                if outflanks:
                    valid_moves[point] = outflanks
        return valid_moves

    def _get_outflanks(self, player: Player, point: Point) -> List[Point]:
        directions = [
            (-1, 1),
            (0, 1),
            (1, 1),
            (-1, 0),
            (1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]
        outflanks = []
        if (
            self._is_on_grid(point)
            and self._grid[point.row][point.col] == disc.get_disc()
        ):
            for direction in directions:
                tmp = self._get_outflanks_in_dir(player, point, direction)
                if tmp:
                    outflanks.extend(tmp)
        return outflanks

    def _get_outflanks_in_dir(
        self, player: Player, point: Point, direction: Tuple[int, int]
    ) -> List[Point]:
        outflanks: List[Point] = []
        next_point = point
        row_dir, col_dir = direction
        while True:
            next_point = Point(next_point.row + row_dir, next_point.col + col_dir)
            if self._is_on_grid(next_point):
                next_value = self._grid[next_point.row][next_point.col]
                if next_value != disc.get_disc():
                    if next_value == disc.get_disc(player):
                        return outflanks
                    outflanks.append(next_point)
                else:
                    break
            else:
                break
        return []

    def _is_on_grid(self, point: Point) -> bool:
        return 0 <= point.row < self.size and 0 <= point.col < self.size
