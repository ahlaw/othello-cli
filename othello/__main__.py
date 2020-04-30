from .agent.human import Human
from .game.game_state import GameState, InvalidMoveError
from .game.player import Player
from .game.point import Point


def point_from_coords(coords: str) -> Point:
    try:
        row, col = [int(x) for x in coords.split(",")]
        return Point(row, col)
    except BaseException:
        raise Exception("Invalid coordinate")


def main() -> None:
    game_state = GameState.new_game(4)
    agents = {}
    agents[Player.BLACK] = Human()
    agents[Player.WHITE] = Human()
    while not game_state.is_over():
        print(game_state.board)
        print(f"Player turn: {game_state.current_player}")
        valid_moves = game_state.legal_moves()
        if valid_moves:
            human_valid_moves = [
                Human.point_to_notation(point) for point in valid_moves
            ]
            print(f"Valid moves: {human_valid_moves}")
            print(f"Valid moves: {valid_moves}")
        else:
            print("No valid moves this turn!")
        while True:
            try:
                move = agents[game_state.current_player].select_move(game_state)
                game_state = game_state.apply_move(move)
                break
            except InvalidMoveError:
                print("Invalid move! Try another move.")
    winner = game_state.winner()
    if winner:
        print(f"The winner is {winner}")
    else:
        print(f"The result is a DRAW")


if __name__ == "__main__":
    main()
