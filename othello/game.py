import copy

from board import Board
from player import Player


class Game:
    def __init__(self, board, current_player, move=None):
        self.board = board
        self.current_player = current_player
        self.last_move = move

    def is_over(self):
        """
        Returns whether game is over given the state.
        """
        pass

    def apply_move(self, move):
        """
        Takes the game state and the move to be applied.
        Returns new game state.
        """
        if move.is_play:
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(self.current_player, move.point)
        else:
            next_board = self.board
        return Game(next_board, self.current_player.other, move)

    def legal_moves(self):
        return self.board.get_valid_moves(self.current_player)

    @classmethod
    def new_game(cls, board_size=8):
        """
        Returns initial state of game.
        """
        board = Board(board_size)
        return cls(board, Player.BLACK)
