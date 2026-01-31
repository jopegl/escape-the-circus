import pygame
import sys

# =====================
# CONFIG
# =====================
WIDTH, HEIGHT = 1000, 800
CELL = 40  # tamanho da grade
WALL_LENGTH = 200

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Editor de Labirinto")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# =====================
# ESTADO
# =====================
walls = []
mode = 'H'  # H ou V

# =====================
# FUNÇÕES
# =====================
def snap(value):
    return (value // CELL) * CELL

def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

def draw_walls():
    for x, y, t in walls:
        if t == 'H':
            pygame.draw.rect(screen, (0, 200, 0), (x, y, WALL_LENGTH, 10))
        else:
            pygame.draw.rect(screen, (0, 200, 0), (x, y, 10, WALL_LENGTH))

def draw_ui():
    text = font.render(f"Modo: {mode} | H/V troca | ENTER exporta", True, (255, 255, 255))
    screen.blit(text, (10, 10))

def export_layout():
    print("\nlayout_labirinto = [")
    for w in walls:
        print(f"    {w},")
    print("]\n")

# =====================
# LOOP PRINCIPAL
# =====================
running = True
while running:
    screen.fill((20, 20, 20))
    draw_grid()
    draw_walls()
    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                mode = 'H'
            elif event.key == pygame.K_v:
                mode = 'V'
            elif event.key == pygame.K_BACKSPACE and walls:
                walls.pop()
            elif event.key == pygame.K_RETURN:
                export_layout()
            elif event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            x = snap(mx)
            y = snap(my)
            walls.append((x, y, mode))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
