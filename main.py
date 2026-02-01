import pygame
import sys
from settings import *
from player import Player
from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3_1 import Level3_1
from levels.level3_2 import Level3_2
pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape The Circus")
CLOCK = pygame.time.Clock()

running = True

player = Player(0, HEIGHT/2 - 20)
level = Level1(player)

pygame.font.init()
font = pygame.font.Font(None, 24)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    level.update()
    if player.proxima_fase:
        if player.proxima_fase == "fase2 - 1":
            level = Level2(player)
            player.hitbox.midbottom = (95, 423)
            player.speed = PLAYER_SPEED

        elif player.proxima_fase == "fase1":
            level = Level1(player)
            player.hitbox.midbottom = (900, 423)
            player.speed = PLAYER_SPEED

        elif player.proxima_fase == "fase3-1":
            level = Level3_1(player)
            player.hitbox.midbottom = (95, 423)
            player.speed = PLAYER_SPEED
        elif player.proxima_fase == "fase2-2":
            level = Level2(player)
            player.hitbox.midbottom = (900, 423)
            player.speed = PLAYER_SPEED
        elif player.proxima_fase == "fase3-2":
            level = Level3_2(player)
            player.hitbox.midbottom = (95, 423)
            player.speed = 2
        elif player.proxima_fase == 'fase3-1-2':
            level = Level3_1(player)
            player.hitbox.midbottom = (120, 423)
            player.speed = PLAYER_SPEED
            
    if player.ganhou:
        level = ending(player)

    # sincroniza sprite com hitbox
    player.rect.midbottom = player.hitbox.midbottom
    player.proxima_fase = None


    level.draw(SCREEN)
    texto = f"x: {player.hitbox.x}  y: {player.hitbox.y}"
    surface_texto = font.render(texto, True, (255, 255, 255))
    SCREEN.blit(surface_texto, (10, 10))


    pygame.display.flip()
    CLOCK.tick(60)

menu(screen, start_the_game)
pygame.quit()
sys.exit()