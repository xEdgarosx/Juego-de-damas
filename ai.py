import random

def get_ai_move(board, ai_pieces):
    # Obtener una lista de movimientos válidos para la IA
    valid_moves = []
    for row, col in ai_pieces:
        for dr in [-1, 1]:
            for dc in [-1, 1]:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < 9
                    and 0 <= new_col < 9
                    and board[new_row][new_col] == 0
                    and is_valid_move(board, row, col, new_row, new_col)
                ):
                    valid_moves.append((row, col, new_row, new_col))

    # Elegir un movimiento aleatorio de la lista de movimientos válidos
    if valid_moves:
        start_row, start_col, end_row, end_col = random.choice(valid_moves)
        board[start_row][start_col] = 0
        board[end_row][end_col] = 2
        ai_pieces.remove((start_row, start_col))
        ai_pieces.add((end_row, end_col))
        return True

    return False

def is_valid_move(board, start_row, start_col, end_row, end_col):
    row_diff = abs(end_row - start_row)
    col_diff = abs(end_col - start_col)

    # Movimiento válido en damas chinas (solo se mueve una casilla en diagonal)
    if row_diff == 1 and col_diff == 1 and board[end_row][end_col] == 0:
        return True

    # Implementar capturas de fichas aquí

    return False