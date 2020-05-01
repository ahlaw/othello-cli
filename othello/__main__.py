import argparse
import time
from typing import Dict, Type

import pkg_resources

from othello import __version__
from othello.agent.base import Agent
from othello.agent.human import Human
from othello.game.game_state import GameState, InvalidMoveError
from othello.game.player import Player


def get_parser() -> argparse.ArgumentParser:
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version", "-v", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "--black", "-b", help="Agent type for black", type=str, default="human"
    )
    parser.add_argument(
        "--white", "-w", help="Agent type for white", type=str, default="human"
    )
    return parser


def get_agents() -> Dict[str, Type[Agent]]:
    """
    Returns dict of agents entrypoints mapped to name.
    """
    agents = {}
    for entry_point in pkg_resources.iter_entry_points("agents"):
        agents[entry_point.name] = entry_point.load()
    return agents


def main() -> None:
    parser = get_parser()
    print(type(parser))
    args = parser.parse_args()

    agents = get_agents()

    player = {}
    player[Player.BLACK] = agents[args.black]()
    player[Player.WHITE] = agents[args.white]()

    game_state = GameState.new_game()

    while not game_state.is_over():
        # ANSI escape sequence to erase display
        print(chr(27) + "[2J")

        print(game_state.board)
        print(f"Player turn: {game_state.current_player}")
        valid_moves = game_state.legal_moves()
        if valid_moves:
            human_valid_moves = [
                Human.point_to_notation(point) for point in valid_moves
            ]
            print(f"Valid moves: {human_valid_moves}")
        else:
            print("No valid moves this turn!")
        while True:
            try:
                move = player[game_state.current_player].select_move(game_state)
                game_state = game_state.apply_move(move)
                break
            except InvalidMoveError:
                print("Invalid move! Try another move.")

        # prevent bots from moving too fast
        time.sleep(0.5)
    winner = game_state.winner()
    if winner:
        print(f"The winner is {winner}")
    else:
        print(f"The result is a DRAW")


if __name__ == "__main__":
    main()
