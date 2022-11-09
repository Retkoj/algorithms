import math

from src.path_finding.simple_min_max_tree_game import MinMaxTreeGame, Player


def number_of_states(n_available_moves, ply):
    """
    Number of possible game states given a ply depth for games where making a move leads to:
    next_available_moves = available_moves - 1

    For example tic tac toe has 9 possible moves at the start and a max ply-depth of 8 (there is 9 - 8 = 1 move left
    in the last round, if the game isn't won yet)

    :param n_available_moves: int, number of available moves at the start of the game
    :param ply: int, depth of lookahead. Full lookahead is (n_available_moves - 1)
    :return: int, number of possible game states
    """
    n_states = 0
    for i in range(1, ply + 1):
        n_states += math.factorial(n_available_moves) / math.factorial((n_available_moves - i))
    return int(n_states)


def minimax(state, ply, player, opponent):
    """
    Recursively evaluates the (game)state tree to find the move that maximizes or minimizes the game outcome,
    depending on the player's goal.

    :param state: MinMaxTreeGame, game state
    :param ply: int, ply, or depth of search/number of moves look-ahead
    :param player: Player enum value, current player
    :param opponent: Player enum value, opponent
    :return: move, score
    """
    best_move, best_score = None, None
    if ply == 0 or len(state.get_valid_moves()) == 0:
        best_score = state.evaluate()
    else:
        for move in state.get_valid_moves():
            state.make_move(move)
            _, score = minimax(state, ply - 1, opponent, player)
            state.undo_move(move)
            if (player == Player.MAX and (best_score is None or score > best_score)) or \
                    (player == Player.MIN and (best_score is None or score < best_score)):
                best_score = score
                best_move = move
    return best_move, best_score


def play_game(player_one, player_two, ply=2):
    """
    Creates a MinMaxTreeGame instance and 'plays' moves until there are no valid moves left

    :param player_one: Player enum value
    :param player_two: Player enum value
    :param ply: int, ply, or depth of search/number of moves look-ahead
    :return: int, end state of the board
    """
    board = MinMaxTreeGame()

    def switch_turn(p1, p2):
        return p2, p1

    while len(board.get_valid_moves()) > 0:
        move, _ = minimax(board, ply, player_one, player_two)
        board.make_move(move)
        player_one, player_two = switch_turn(player_one, player_two)

    return board.evaluate()


if __name__ == '__main__':
    """
    Given the following tree and ply=2, the best moves when the MAX player is starting would lead to 3,
    if the MIN player starts it would be 5.
    root
    ├── l1
    │   ├── l1-1: 3
    │   └── l1-2: 5
    └── r1
        ├── r1-1: 2
        └── r1-2: 9
    """
    assert play_game(Player.MAX, Player.MIN) == 3
    assert play_game(Player.MIN, Player.MAX) == 5

    assert number_of_states(10, 6) == 187300
    assert number_of_states(9, 8) == 623529
