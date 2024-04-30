import pygame
import sys
import subprocess

# Función para dibujar texto en la pantalla
def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Función para crear botones
def create_button(screen, text, font, color, x, y, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, color, (x, y, width, height))
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    draw_text(screen, text, font, (255, 255, 255), x + width / 2, y + height / 2)

# Funciones para las acciones de los botones
def set_easy_difficulty():
    global difficulty
    difficulty = 'Fácil'
    start_game(difficulty)

def set_medium_difficulty():
    global difficulty
    difficulty = 'Medio'
    start_game(difficulty)

def set_hard_difficulty():
    global difficulty
    difficulty = 'Difícil'
    start_game(difficulty)

def start_game(difficulty):
    subprocess.run(["python", "main.py", difficulty])

# Inicializar Pygame
pygame.init()

# Configurar la ventana del menú
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Menú de Selección de Dificultad")

# Definir fuentes
font = pygame.font.Font(None, 36)

# Bucle principal del menú
running = True
difficulty = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Crear botones de dificultad
    button_width = 200
    button_height = 50
    button_spacing = 20
    button_x = (WINDOW_WIDTH - button_width) / 2
    button_y = WINDOW_HEIGHT / 2 - (button_height + button_spacing) * 1.5

    create_button(screen, "Fácil", font, (0, 255, 0), button_x, button_y, button_width, button_height, set_easy_difficulty)

    button_y += button_height + button_spacing
    create_button(screen, "Medio", font, (255, 255, 0), button_x, button_y, button_width, button_height, set_medium_difficulty)

    button_y += button_height + button_spacing
    create_button(screen, "Difícil", font, (255, 0, 0), button_x, button_y, button_width, button_height, set_hard_difficulty)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
