import re

from .base import Agent
from ..game.game_state import GameState
from ..game.move import Move
from ..game.point import Point


class InvalidInputError(Exception):
    """Exception class for when input is not a valid move selection."""

    pass


class Human(Agent):
    def select_move(self, game_state: GameState) -> Move:
        """Select move using user input."""
        while True:
            try:
                move_input: str = input("Enter your move: ").strip().lower()
                self._validate_input(move_input)
                return self._notation_to_point(move_input)
            except InvalidInputError:
                print("Invalid input! Please try again.")

    @staticmethod
    def point_to_notation(point: Point) -> str:
        letter: str = chr(point.col + ord("a"))
        number: str = str(point.row + 1)
        return f"{letter}{number}"

    @staticmethod
    def _notation_to_point(move_input: str) -> Move:
        if move_input == "pass":
            return Move.pass_turn()
        elif move_input == "resign":
            return Move.resign()
        else:
            letter, number = move_input
            col: int = ord(letter) - ord("a")
            row: int = int(number) - 1
            return Move.play(Point(row, col))

    @staticmethod
    def _validate_input(move_input: str) -> None:
        pattern = "^([a-z]([1-9]|1[0-9]|2[0-6])|pass|resign)$"

        valid = re.match(pattern, move_input)
        if not valid:
            raise InvalidInputError("Input is not a valid move!")
