import copy

from .board import Board, InvalidStonePlacementError
from .player import Player


class InvalidMoveError(Exception):
    """
    Exception class for passing on a turn when there are
    legal stone placements.
    """
    pass


class GameState:
    """
    Game class representing the current game state of
    an Othello game.
    """
    def __init__(self, board, current_player, move=None, prev_move=False):
        self.board = board
        self.current_player = current_player
        self.last_move = move
        self.second_last_move = prev_move

    def apply_move(self, move):
        """
        Takes the game state and the move to be applied.
        Returns new game state.
        """
        if move.is_play:
            next_board = copy.deepcopy(self.board)
            try:
                next_board.place_stone(self.current_player, move.point)
            except InvalidStonePlacementError:
                raise InvalidMoveError(f'Cannot place the stone at {move.point}')
        else:
            if move.is_pass and self.legal_moves():
                raise InvalidMoveError('Cannot pass when there are legal moves!')
            next_board = self.board
        return GameState(next_board, self.current_player.other, move, self.last_move)

    def legal_moves(self):
        """
        Returns list of moves that are legal plays for the current player.
        """
        return list(self.board.get_valid_moves(self.current_player).keys())

    def is_over(self):
        """
        Returns whether game is over given the current state.
        """
        if not self.last_move:
            return False
        if self.last_move.is_resign:
            return True
        if not self.second_last_move:
            return False
        return self.last_move.is_pass and self.second_last_move.is_pass

    def winner(self):
        """
        Returns player who has not resigned if one has resigned.
        If neither player has resigned, returns player with the most
        stones on the board. If it is a draw, None is returned.
        """
        if self.last_move and self.last_move.is_resign:
            return self.current_player
        black_count = self.board.count_stones(Player.BLACK)
        white_count = self.board.count_stones(Player.WHITE)
        if black_count > white_count:
            return Player.BLACK
        elif white_count > black_count:
            return Player.WHITE
        else:
            return None

    @classmethod
    def new_game(cls, board_size=8):
        """
        Returns initial state of game.
        """
        board = Board(board_size)
        return cls(board, Player.BLACK)
