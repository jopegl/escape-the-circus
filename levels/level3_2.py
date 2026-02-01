from level import Level
import pygame
import os 
from settings import *

class Level3_2(Level):
    def __init__(self, player):
        super().__init__(player)

        bg_path = os.path.join('assets', 'backgrounds','lvl3', 'BACKGROUND3.png')
        self.background = pygame.image.load(bg_path).convert_alpha()

        self.walls = [
            pygame.Rect(0, 0, WIDTH, 1),  

            pygame.Rect(0, HEIGHT - 1, WIDTH, 1),  


            pygame.Rect(0, 0, 1, HEIGHT),  

            pygame.Rect(WIDTH - 1, 0, 1, HEIGHT)

        ]

        self.interacoes = [

            # Porta / saída (parte de baixo – maleta)
            {
                "rect": pygame.Rect(WIDTH - 90, 360, 120, 140),
                "tipo": "final",
                "categoria": "final"
            },
        ]



        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT)
        )

    def draw(self, screen):

        screen.blit(self.background, (0, 0))

        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 100, 200, 80)) 
        screen.blit(overlay, (0, 0))

        dark_overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        for wall in self.walls:
            surf = pygame.Surface((wall.width, wall.height), pygame.SRCALPHA)
            pygame.draw.rect(surf, (0, 200, 0, 100), surf.get_rect())
            screen.blit(surf, wall.topleft)

        for zona in self.interacoes:
            rect = zona["rect"]
            surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            pygame.draw.rect(surf, (0, 0, 200, 100), surf.get_rect())
            screen.blit(surf, rect.topleft)

        self.player.draw(screen)
