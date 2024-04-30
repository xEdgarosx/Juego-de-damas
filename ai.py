import copy

BOARD_SIZE = 9

def get_all_moves(board, pieces):
    moves = []
    for row, col in pieces:
        for dr in [-1, 1]:
            for dc in [-1, 1]:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < BOARD_SIZE
                    and 0 <= new_col < BOARD_SIZE
                    and board[new_row][new_col] == 0
                    and is_valid_move(board, row, col, new_row, new_col)
                ):
                    moves.append((row, col, new_row, new_col))
                elif (
                    0 <= new_row + dr < BOARD_SIZE
                    and 0 <= new_col + dc < BOARD_SIZE
                    and board[new_row + dr][new_col + dc] == 0
                    and board[new_row][new_col] == 1
                    and is_valid_capture(board, row, col, new_row + dr, new_col + dc)
                ):
                    moves.append((row, col, new_row + dr, new_col + dc))
    return moves

def evaluate_board(board, ai_pieces, player_pieces):
    ai_count = len(ai_pieces)
    player_count = len(player_pieces)
    return ai_count - player_count

def minimax(board, ai_pieces, player_pieces, depth, is_maximizing):
    if depth == 0:
        return evaluate_board(board, ai_pieces, player_pieces)

    if is_maximizing:
        best_score = float('-inf')
        for move in get_all_moves(board, ai_pieces):
            new_board = copy.deepcopy(board)
            new_ai_pieces = copy.copy(ai_pieces)
            new_player_pieces = copy.copy(player_pieces)

            start_row, start_col, end_row, end_col = move
            new_board[start_row][start_col] = 0
            new_board[end_row][end_col] = 2
            new_ai_pieces.remove((start_row, start_col))
            new_ai_pieces.add((end_row, end_col))

            if abs(end_row - start_row) == 2:  # Captura de ficha
                capture_row = (start_row + end_row) // 2
                capture_col = (start_col + end_col) // 2
                new_board[capture_row][capture_col] = 0
                new_player_pieces.remove((capture_row, capture_col))

            score = minimax(new_board, new_player_pieces, new_ai_pieces, depth - 1, False)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_all_moves(board, player_pieces):
            new_board = copy.deepcopy(board)
            new_ai_pieces = copy.copy(ai_pieces)
            new_player_pieces = copy.copy(player_pieces)

            start_row, start_col, end_row, end_col = move
            new_board[start_row][start_col] = 0
            new_board[end_row][end_col] = 1
            new_player_pieces.remove((start_row, start_col))
            new_player_pieces.add((end_row, end_col))

            score = minimax(new_board, new_ai_pieces, new_player_pieces, depth - 1, True)
            best_score = min(best_score, score)
        return best_score

def get_ai_move(board, ai_pieces, player_pieces, difficulty):
    if difficulty == 'Fácil':
        depth = 1
    elif difficulty == 'medio':
        depth = 3
    elif difficulty == 'Difícil':
        depth = 4

    best_move = None
    best_score = float('-inf')

    for move in get_all_moves(board, ai_pieces):
        new_board = copy.deepcopy(board)
        new_ai_pieces = copy.copy(ai_pieces)
        new_player_pieces = copy.copy(player_pieces)

        start_row, start_col, end_row, end_col = move
        new_board[start_row][start_col] = 0
        new_board[end_row][end_col] = 2
        new_ai_pieces.remove((start_row, start_col))
        new_ai_pieces.add((end_row, end_col))

        if abs(end_row - start_row) == 2:  # Captura de ficha
            capture_row = (start_row + end_row) // 2
            capture_col = (start_col + end_col) // 2
            new_board[capture_row][capture_col] = 0
            new_player_pieces.remove((capture_row, capture_col))

        score = minimax(new_board, new_ai_pieces, new_player_pieces, depth - 1, False)
        if score > best_score:
            best_score = score
            best_move = move

    if best_move:
        start_row, start_col, end_row, end_col = best_move
        board[start_row][start_col] = 0
        board[end_row][end_col] = 2
        ai_pieces.remove((start_row, start_col))
        ai_pieces.add((end_row, end_col))

        if abs(end_row - start_row) == 2:  # Captura de ficha
            capture_row = (start_row + end_row) // 2
            capture_col = (start_col + end_col) // 2
            board[capture_row][capture_col] = 0
            player_pieces.remove((capture_row, capture_col))

        return True

    return False

def is_valid_move(board, start_row, start_col, end_row, end_col):
    row_diff = abs(end_row - start_row)
    col_diff = abs(end_col - start_col)

    # Movimiento válido en damas chinas (solo se mueve una casilla en diagonal)
    if row_diff == 1 and col_diff == 1 and board[end_row][end_col] == 0:
        return True

    # Captura de ficha
    if row_diff == 2 and col_diff == 2 and board[end_row][end_col] == 0:
        return is_valid_capture(board, start_row, start_col, end_row, end_col)

    return False

def is_valid_capture(board, start_row, start_col, end_row, end_col):
    capture_row = (start_row + end_row) // 2
    capture_col = (start_col + end_col) // 2
    return board[capture_row][capture_col] == 1  # Hay una ficha del jugador para capturar
