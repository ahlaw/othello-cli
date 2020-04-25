from player import Player
from point import Point
from stone import StoneFactory

MIN_BOARD_SIZE = 4
MAX_BOARD_SIZE = 28

class BoardSizeError(Exception):
    pass

class InvalidMoveError(Exception):
    pass

class Board():
    def __init__(self, size):
        if (not MIN_BOARD_SIZE <= size or
            not MAX_BOARD_SIZE >= size or
            size % 2 != 0):
            raise BoardSizeError(f'{size} is invalid size!')

        self.size = size

        self.stone = StoneFactory()


        center = size // 2 - 1
        self._grid = [[self.stone()] * size for _ in range(size)]
        self._grid[center][center] = self.stone(Player.WHITE)
        self._grid[center][center+1] = self.stone(Player.BLACK)
        self._grid[center+1][center] = self.stone(Player.BLACK)
        self._grid[center+1][center+1] = self.stone(Player.WHITE)

        self.valid_moves = {}

    def __str__(self):
        return '\n'.join(f'{row}' for row in self._grid)

    def place_stone(self, player, point):
        valid_moves = self.get_valid_moves(player)

        if point not in valid_moves:
            raise InvalidMoveError(f'{point} is not a valid move!')

        self._grid[point.col][point.row] = self.stone(player)
        capturables = valid_moves[point]
        for row, col in capturables:
            self._grid[col][row] = self.stone(player)

    def get_valid_moves(self, player):
        valid_moves = {}
        for col in range(self.size):
            for row in range(self.size):
                point = Point(row, col)
                capturables = self._get_capturables(player, point)
                if capturables:
                    valid_moves[point] = capturables
        return valid_moves

    def _get_capturables(self, player, point):
        directions = [
                        (-1,  1), (0,  1), (1,  1),
                        (-1,  0),          (1,  0),
                        (-1, -1), (0, -1), (1, -1)
                    ]
        capturables = []
        if (self._is_on_grid(point) and
            self._grid[point.col][point.row] == self.stone()):
            for direction in directions:
                tmp = self._get_capturables_in_dir(player, point, direction)
                if tmp:
                    capturables.extend(tmp)
        return capturables

    def _get_capturables_in_dir(self, player, point, direction):
        capturables = []
        next_point = point
        row_dir, col_dir = direction
        while True:
            next_point = Point(next_point.row + row_dir,
                               next_point.col + col_dir)
            if self._is_on_grid(next_point):
                next_value = self._grid[next_point.col][next_point.row]
                if next_value != self.stone():
                    if next_value == self.stone(player):
                        return capturables
                    capturables.append(next_point)
                else:
                    break
            else:
                break
        return []

    def _is_on_grid(self, point):
        return (0 <= point.row < self.size and
                0 <= point.col < self.size)
