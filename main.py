from othello.game import Game
from othello.move import Move
from othello.point import Point


def point_from_coords(coords):
    try:
        coords = [int(x) for x in coords.split(',')]
        assert(len(coords) == 2)
        row, col = coords
        return Point(row, col)
    except:
        raise Exception('Invalid coordinate')


if __name__ == '__main__':
    game = Game.new_game()
    while not game.is_over():
        print(game.board)
        print(game.current_player)
        valid_moves = game.legal_moves()
        if not valid_moves: 
            move = Move(is_pass=True)
        else:
            print(valid_moves)
            human_move = input('Enter your move: ')
            point = point_from_coords(human_move.strip())
            move = Move(point)
        game = game.apply_move(Move.play(point))
