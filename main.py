import pygame
from board import draw_board, get_tile_coords, is_valid_move
from pieces import select_piece, move_piece, initialize_board
from ai import get_ai_move

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
                if is_valid_move(board, start_row, start_col, row, col):
                    move_piece(board, player_pieces, ai_pieces, start_row, start_col, row, col)
                    # Turno de la IA
                    get_ai_move(board, ai_pieces)
                    selected_piece = None

    # Dibujar el tablero y las fichas
    draw_board(screen, board, player_pieces, ai_pieces, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()