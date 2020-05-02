"""Human agent module."""
import re

from othello.agent.base import Agent
from othello.game.game_state import GameState
from othello.game.move import Move
from othello.game.point import Point


class InvalidInputError(Exception):
    """Exception class for when input is not a valid move selection."""

    pass


class NotationError(Exception):
    """Exception class for when game notation related errors."""


class Human(Agent):
    """Human agent."""

    def select_move(self, game_state: GameState) -> Move:
        """Select move using user input.

        Args:
            game_state: Current game state.

        Returns:
            Move instance.
        """
        while True:
            try:
                move_input: str = input("Enter your move: ").strip().lower()
                self.validate_input(move_input)
                return self.notation_to_move(move_input)
            except InvalidInputError:
                print("Invalid input! Please try again.")

    @staticmethod
    def point_to_notation(point: Point) -> str:
        """Convert Point instance to notation string.

        Args:
            point: Point to be converted.

        Returns:
            Notation.

        Raises:
            NotationError: No notation exists for given point.
        """
        if not (0 <= point.row <= 26 and 0 <= point.col <= 26):
            raise NotationError("Notation unavailable for point")
        letter: str = chr(point.col + ord("a"))
        number: str = str(point.row + 1)
        return f"{letter}{number}"

    @staticmethod
    def notation_to_move(move_input: str) -> Move:
        """Convert notation string to Point instance.

        Args:
            move_input: Notation to be converted.

        Returns:
            Move.
        """
        if move_input == "pass":
            return Move.pass_turn()
        elif move_input == "resign":
            return Move.resign()
        else:
            col: int = ord(move_input[0]) - ord("a")
            row: int = int(move_input[1:]) - 1
            return Move.play(Point(row, col))

    @staticmethod
    def validate_input(move_input: str) -> None:
        """Validate human input.

        Args:
            move_input: Notation input.

        Raises:
            InvalidInputError: Input is not valid move notation.
        """
        pattern = "^([a-z]([1-9]|1[0-9]|2[0-6])|pass|resign)$"

        valid = re.match(pattern, move_input)
        if not valid:
            raise InvalidInputError("Input is not a valid move!")
