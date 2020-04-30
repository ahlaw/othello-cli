from abc import ABC, abstractmethod

from ..game.game_state import GameState
from ..game.move import Move


class Agent(ABC):
    """Agent abstract base class."""

    @abstractmethod
    def select_move(self, game_state: GameState) -> Move:
        """Select move given game state."""
        pass
