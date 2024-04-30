import pygame
from board import draw_board, get_tile_coords, is_valid_move, is_valid_capture
from pieces import select_piece, move_piece, initialize_board
from ai import get_ai_move

import sys

# Obtener la dificultad del argumento pasado al script
if len(sys.argv) > 1:
    difficulty = sys.argv[1]

print(difficulty)

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Damas Chinas")

# Inicializar el tablero
board, player_pieces, ai_pieces = initialize_board()

# Bucle principal del juego
running = True
selected_piece = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Manejar clic del mouse
            row, col = get_tile_coords(event.pos, WINDOW_WIDTH, WINDOW_HEIGHT)
            if (row, col) in player_pieces:  # Seleccionar ficha del jugador
                selected_piece = (row, col)
            elif selected_piece:
                start_row, start_col = selected_piece
                if is_valid_move(board, start_row, start_col, row, col, player_pieces, ai_pieces):
                    move_piece(board, player_pieces, ai_pieces, start_row, start_col, row, col)
                    if abs(row - start_row) == 2:  # Captura de ficha
                        capture_row = (start_row + row) // 2
                        capture_col = (start_col + col) // 2
                        ai_pieces.remove((capture_row, capture_col))
                    # Turno de la IA
                    get_ai_move(board, ai_pieces, player_pieces, difficulty)
                    selected_piece = None

    # Dibujar el tablero y las fichas
    draw_board(screen, board, player_pieces, ai_pieces, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()