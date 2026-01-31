import pygame
import sys
from settings import *
from player import Player
from levels.level1 import Level1
from levels.level2 import Level2
pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape The Circus")
CLOCK = pygame.time.Clock()

running = True

player = Player(0,HEIGHT/2)
level = Level1(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    level.update()
    if player.proxima_fase:
        if player.proxima_fase == "fase2 - 1":
            level = Level2(player)
            player.rect.topleft = (0, HEIGHT//2) 
        elif player.proxima_fase == "fase1":
            level = Level1(player)
        elif player.proxima_fase == "fase3 - 1":
            pass
        player.proxima_fase = None

    level.draw(SCREEN)

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
sys.exit()