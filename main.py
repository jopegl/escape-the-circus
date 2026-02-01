import pygame
import sys
from settings import *
from player import Player
from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3_1 import Level3_1
from levels.level3_2 import Level3_2
from levels.ending import Ending
from menu import menu
import pygame_menu
from utils import *
import sys
import os

pygame.init()
pygame.mixer.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape The Circus")
CLOCK = pygame.time.Clock()

MUSIC_PATH = os.path.join('assets', 'sounds', 'mainsong.mp3')
pygame.mixer.music.load(MUSIC_PATH)
pygame.mixer.music.set_volume(0.4)  
pygame.mixer.music.play(-1)  


def start_game():
    player = Player(0, HEIGHT/2 - 20)
    level = Level1(player)

    pygame.font.init()

    hud_font = pygame.font.Font(
        pygame_menu.font.FONT_8BIT,
        18
    )

    running = True
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
                
        if player.ganhou and not isinstance(level, Ending):
            level = Ending()

        if isinstance(level, Ending) and level.finished:
            running = False

        # sincroniza sprite com hitbox
        player.rect.midbottom = player.hitbox.midbottom
        player.proxima_fase = None


        level.draw(SCREEN)
        draw_mask_hud_text(SCREEN, player, hud_font)


        pygame.display.flip()
        CLOCK.tick(60)

menu(SCREEN, start_game)

pygame.quit()
sys.exit()