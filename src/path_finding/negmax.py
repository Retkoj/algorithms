from src.path_finding.simple_min_max_tree_game import MinMaxTreeGame, Player


def negmax(state, ply, player, opponent):
    """
    Recursively evaluates the (game)state tree to find the move that maximizes the game outcome,
    by negating the values of the nodes. Negating the values simulates one player wanting to maximize, and
    one player wanting to minimize the outcome.

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
            _, score = negmax(state, ply - 1, opponent, player)
            state.undo_move(move)
            if best_score is None or (-1 * score) > best_score:
                best_score = -1 * score
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
        move, _ = negmax(board, ply, player_one, player_two)
        board.make_move(move)
        player_one, player_two = switch_turn(player_one, player_two)

    return board.evaluate()


if __name__ == '__main__':
    """
    (The current implementation of) NegMax always assumes the maximizing strategy. 
    Given the following tree and ply=2, the best moves for a maximizing strategy would lead to 3
    
    root
    ├── l1
    │   ├── l1-1: 3
    │   └── l1-2: 5
    └── r1
        ├── r1-1: 2
        └── r1-2: 9
    """
    assert play_game(Player.MAX, Player.MIN) == 3
