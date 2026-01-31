import pygame
import sys
from settings import *
from player import Player
from levels.level1 import Level1
pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape The Circus")
CLOCK = pygame.time.Clock()

running = True

player = Player(100,100)
level = Level1(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    level.update()
    level.draw(SCREEN)

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
sys.exit()