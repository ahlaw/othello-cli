from .game.game_state import GameState
from .game.move import Move
from .game.point import Point


def point_from_coords(coords: str) -> Point:
    try:
        row, col = [int(x) for x in coords.split(",")]
        return Point(row, col)
    except BaseException:
        raise Exception("Invalid coordinate")


def main() -> None:
    game = GameState.new_game()
    while not game.is_over():
        print(game.board)
        print(game.current_player)
        valid_moves = game.legal_moves()
        if not valid_moves:
            move = Move(is_pass=True)
        else:
            print(valid_moves)
            human_move = input("Enter your move: ")
            point = point_from_coords(human_move.strip())
            move = Move.play(point)
        game = game.apply_move(move)


if __name__ == "__main__":
    main()
