import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

walls = []

HORIZONTAL = True
WALL_THICKNESS = 20
WALL_LENGTH = 120

font = pygame.font.SysFont(None, 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                HORIZONTAL = not HORIZONTAL

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if HORIZONTAL:
                rect = pygame.Rect(x, y, WALL_LENGTH, WALL_THICKNESS)
            else:
                rect = pygame.Rect(x, y, WALL_THICKNESS, WALL_LENGTH)

            walls.append(rect)
            print(rect)

    screen.fill((0, 0, 0))

    for wall in walls:
        pygame.draw.rect(screen, (0, 200, 0), wall)

    mode_text = "HORIZONTAL" if HORIZONTAL else "VERTICAL"
    text = font.render(f"Modo: {mode_text} | R para alternar", True, (255,255,255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
