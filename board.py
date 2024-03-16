import pygame

BOARD_SIZE = 9

def draw_board(screen, board, player_pieces, ai_pieces, window_width, window_height):
    tile_size = min(window_width, window_height) // BOARD_SIZE
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
            color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, rect)

    # Dibujar las fichas del jugador
    for row, col in player_pieces:
        x = col * tile_size + tile_size // 2
        y = row * tile_size + tile_size // 2
        pygame.draw.circle(screen, (255, 0, 0), (x, y), tile_size // 3)

    # Dibujar las fichas de la IA
    for row, col in ai_pieces:
        x = col * tile_size + tile_size // 2
        y = row * tile_size + tile_size // 2
        pygame.draw.circle(screen, (0, 0, 255), (x, y), tile_size // 3)

def get_tile_coords(pos, window_width, window_height):
    x, y = pos
    tile_size = min(window_width, window_height) // BOARD_SIZE
    row = y // tile_size
    col = x // tile_size
    return row, col

def is_valid_move(board, start_row, start_col, end_row, end_col):
    row_diff = abs(end_row - start_row)
    col_diff = abs(end_col - start_col)

    # Movimiento válido en damas chinas (solo se mueve una casilla en diagonal)
    if row_diff == 1 and col_diff == 1 and board[end_row][end_col] == 0:
        return True

    # Implementar capturas de fichas aquí

    return False