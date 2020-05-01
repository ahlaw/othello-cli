import random

from othello.agent.base import Agent
from othello.game.game_state import GameState
from othello.game.move import Move


class RandomBot(Agent):
    def select_move(self, game_state: GameState) -> Move:
        """Choose a random valid move."""
        candidates = game_state.legal_moves()
        if not candidates:
            return Move.pass_turn()
        return Move.play(random.choice(candidates))
