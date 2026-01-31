from level import Level
import pygame
import os 
from settings import *

class Level1(Level):
    def __init__(self, player):
        super().__init__(player)

        bg_path = os.path.join('assets', 'backgrounds', 'BACKGROUND1.png')
        self.background = pygame.image.load(bg_path).convert()


        self.walls = [
            pygame.Rect(0, 40, WIDTH, 180), #cima 
            
            #esquerda
            pygame.Rect(0, 60, 120, 300),  
            pygame.Rect(0, 500, 120, 300),

            #direita
            pygame.Rect(WIDTH - 115, 60, 120, 300),  
            pygame.Rect(WIDTH - 115, 500, 120, 300),

            pygame.Rect(0, HEIGHT - 40, WIDTH, 40), #baixo
        ]


        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT)
        )
    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        for wall in self.walls:
            surf = pygame.Surface((wall.width, wall.height), pygame.SRCALPHA)
            pygame.draw.rect(surf, (0, 200, 0, 100), surf.get_rect())
            screen.blit(surf, wall.topleft)

        self.player.draw(screen)
