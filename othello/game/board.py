from typing import Dict, List, Tuple

from .player import Player
from .point import Point
from .stone import StoneFactory

MIN_BOARD_SIZE = 4
MAX_BOARD_SIZE = 26


class BoardSizeError(Exception):
    """
    Exception class for invalid board sizes when initializing Board object.
    """

    pass


class InvalidStonePlacementError(Exception):
    """
    Exception class for placing stone on Board at an invalid location.
    """

    pass


class Board:
    """
    Board class representing an Othello board with white
    and black stones.
    """

    def __init__(self, size: int) -> None:
        if not MIN_BOARD_SIZE <= size or not MAX_BOARD_SIZE >= size or size % 2 != 0:
            raise BoardSizeError(f"{size} is invalid size!")

        self.size = size

        self.stone = StoneFactory()

        center = size // 2 - 1
        self._grid = [[self.stone()] * size for _ in range(size)]
        self._grid[center][center] = self.stone(Player.WHITE)
        self._grid[center][center + 1] = self.stone(Player.BLACK)
        self._grid[center + 1][center] = self.stone(Player.BLACK)
        self._grid[center + 1][center + 1] = self.stone(Player.WHITE)

    def __str__(self) -> str:
        return "\n".join(f"{row}" for row in self._grid)

    def count_stones(self, player: Player) -> int:
        """
        Counts the number of stones on the board corresponding
        to the given player
        """
        count = 0
        player_stone = self.stone(player)
        for i in range(self.size):
            for j in range(self.size):
                if self._grid[i][j] == player_stone:
                    count += 1
        return count

    def place_stone(self, player: Player, point: Point) -> None:
        """
        Place stone corresponding to player color at the
        given point if it is a valid move.
        """
        valid_moves = self.get_valid_moves(player)

        if point not in valid_moves:
            raise InvalidStonePlacementError(f"{point} is not a valid move!")

        self._grid[point.row][point.col] = self.stone(player)
        capturables = valid_moves[point]
        for row, col in capturables:
            self._grid[row][col] = self.stone(player)

    def get_valid_moves(self, player: Player) -> Dict[Point, List[Point]]:
        """
        Returns a dictionary of where the keys are valid stone
        placements for the given player and the values are the
        stones that will be captured upon playing the move.
        """
        valid_moves = {}
        for row in range(self.size):
            for col in range(self.size):
                point = Point(row, col)
                capturables = self._get_capturables(player, point)
                if capturables:
                    valid_moves[point] = capturables
        return valid_moves

    def _get_capturables(self, player: Player, point: Point) -> List[Point]:
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
        capturables = []
        if self._is_on_grid(point) and self._grid[point.row][point.col] == self.stone():
            for direction in directions:
                tmp = self._get_capturables_in_dir(player, point, direction)
                if tmp:
                    capturables.extend(tmp)
        return capturables

    def _get_capturables_in_dir(
        self, player: Player, point: Point, direction: Tuple[int, int]
    ) -> List[Point]:
        capturables: List[Point] = []
        next_point = point
        row_dir, col_dir = direction
        while True:
            next_point = Point(next_point.row + row_dir, next_point.col + col_dir)
            if self._is_on_grid(next_point):
                next_value = self._grid[next_point.row][next_point.col]
                if next_value != self.stone():
                    if next_value == self.stone(player):
                        return capturables
                    capturables.append(next_point)
                else:
                    break
            else:
                break
        return []

    def _is_on_grid(self, point: Point) -> bool:
        return 0 <= point.row < self.size and 0 <= point.col < self.size
