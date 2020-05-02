"""Abstract base class for agents."""
from abc import ABC, abstractmethod

from othello.game.game_state import GameState
from othello.game.move import Move


class Agent(ABC):
    """Agent abstract base class."""

    @abstractmethod
    def select_move(self, game_state: GameState) -> Move:
        """Select move given game state."""
        pass
