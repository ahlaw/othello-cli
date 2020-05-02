"""Random bot agent module."""
import random

from othello.agent.base import Agent
from othello.game.game_state import GameState
from othello.game.move import Move


class RandomBot(Agent):
    """RandomBot agent."""

    def select_move(self, game_state: GameState) -> Move:
        """Choose a random valid move.

        Args:
            game_state: Current game state.

        Returns:
            Move instance.
        """
        candidates = game_state.legal_moves()
        if not candidates:
            return Move.pass_turn()
        return Move.play(random.choice(candidates))
