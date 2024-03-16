BOARD_SIZE = 9

def initialize_board():
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    player_pieces = set()
    ai_pieces = set()

    # Colocar fichas iniciales del jugador
    for row in range(3):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:
                board[row][col] = 1
                player_pieces.add((row, col))

    # Colocar fichas iniciales de la IA
    for row in range(BOARD_SIZE - 3, BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:
                board[row][col] = 2
                ai_pieces.add((row, col))

    return board, player_pieces, ai_pieces

def select_piece(row, col):
    # Lógica para seleccionar una ficha
    pass

def move_piece(board, player_pieces, ai_pieces, start_row, start_col, end_row, end_col):
    # Mover la ficha seleccionada
    board[start_row][start_col] = 0
    board[end_row][end_col] = 1
    player_pieces.remove((start_row, start_col))
    player_pieces.add((end_row, end_col))