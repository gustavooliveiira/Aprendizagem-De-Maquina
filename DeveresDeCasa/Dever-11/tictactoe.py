"""
Tic Tac Toe Player
"""
import math
import copy


X = "X"
O = "O"
EMPTY = None # CORRIGIDO: Nome da constante deve ser 'EMPTY'


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    if count_X == count_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: # CORRIGIDO: Usando 'EMPTY'
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")

    # CORRIGIDO: Indentação movida para fora do 'if'
    new_board = copy.deepcopy(board)
    current_player = player(board)
    i, j = action # CORRIGIDO: Deve ser '=' para atribuição
    new_board[i][j] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY: # CORRIGIDO: Usando 'EMPTY'
            return board[i][0]
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY: # CORRIGIDO: Usando 'EMPTY'
            return board[0][j]
    # Check diagonals
    # CORRIGIDO: Indentação movida para fora do loop 'for j'
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY: # CORRIGIDO: Usando 'EMPTY'
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY: # CORRIGIDO: Usando 'EMPTY'
        return board[0][2]

    return None # CORRIGIDO: Indentação movida para o nível mais externo da função


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    # Check if all cells are filled
    for row in board:
        if EMPTY in row: # CORRIGIDO: Usando 'EMPTY'
            return False
    return True # CORRIGIDO: Indentação movida para fora do loop 'for row'


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        # Maximize for X
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    else:
        # Minimize for O
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action


def max_value(board):
    """
    Helper function for minimax, representing the maximizing player (X).
    """
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    Helper function for minimax, representing the minimizing player (O).
    """
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v