"""Game state module."""
from __future__ import annotations

import copy
from typing import List, Optional

from othello.game.board import Board, InvalidDiscPlacementError
from othello.game.move import Move
from othello.game.player import Player
from othello.game.point import Point


class InvalidMoveError(Exception):
    """Raised when passing while there are legal disc placements."""

    pass


class GameState:
    """An Othello game state.

    Attributes:
        board: Board instance reflecting current state.
        current_player: Player whose turn it is.
        last_move: The last Move played.
        second_last_move: The second to last Move played.
    """

    def __init__(
        self,
        board: Board,
        current_player: Player,
        move: Optional[Move] = None,
        prev_move: Optional[Move] = None,
    ) -> None:
        """Default constructor for GameState.

        Args:
            board: Board instance reflecting current state.
            current_player: Player whose turn it is.
            move: Move that was played.
            prev_move: Previous Move played.
        """
        self.board = board
        self.current_player = current_player
        self.last_move = move
        self.second_last_move = prev_move

    def apply_move(self, move: Move) -> GameState:
        """Apply Move to GameState.

        Args:
            move: Move to be applied.

        Returns:
            New GameState instance.

        Raises:
            InvalidMoveError: If the move is illegal given the game state.
        """
        if move.is_play and move.point is not None:
            next_board = copy.deepcopy(self.board)
            try:
                next_board.place_disc(self.current_player, move.point)
            except InvalidDiscPlacementError:
                raise InvalidMoveError(f"Cannot place the disc at {move.point}")
        else:
            if move.is_pass and self.legal_moves():
                raise InvalidMoveError("Cannot pass when there are legal moves!")
            next_board = self.board
        return GameState(next_board, self.current_player.other, move, self.last_move)

    def legal_moves(self) -> List[Point]:
        """Returns list of legal plays for the current player.

        Returns:
            List of Point instances that are legal plays.
        """
        return list(self.board.get_valid_moves(self.current_player).keys())

    def is_over(self) -> bool:
        """Returns whether game is over given the current state.

        Returns:
            True if game is over, False otherwise.
        """
        if not self.last_move:
            return False
        if self.last_move.is_resign:
            return True
        if not self.second_last_move:
            return False
        return self.last_move.is_pass and self.second_last_move.is_pass

    def winner(self) -> Optional[Player]:
        """Returns whether game is over.

        If a player has resigned, the other player is the winner. If
        neither player has resigned, the winner is the player with the
        most discs on the board. If they have an equal count, it is a
        draw.

        Returns:
            Player who won if there is a winner, None if it is a draw.
        """
        if self.last_move and self.last_move.is_resign:
            return self.current_player
        black_count = self.board.count_discs(Player.BLACK)
        white_count = self.board.count_discs(Player.WHITE)
        if black_count > white_count:
            return Player.BLACK
        elif white_count > black_count:
            return Player.WHITE
        else:
            return None

    @classmethod
    def new_game(cls, board_size: int = 8) -> GameState:
        """Constructor for initial game state.

        Args:
            board_size: Board size.

        Returns:
            Initial game state.
        """
        board = Board(board_size)
        return cls(board, Player.BLACK)
