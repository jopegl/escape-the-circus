from level import Level
import pygame
import os 
from settings import *

class Level1(Level):
    def __init__(self, player):
        super().__init__(player)

        bg_path = os.path.join('assets', 'backgrounds','lvl1', 'BACKGROUND1MASK.png')
        self.background = pygame.image.load(bg_path).convert()
        background_no_mask_path = os.path.join('assets', 'backgrounds','lvl1', 'BACKGROUND1.png')
        self.background_no_mask = pygame.image.load(background_no_mask_path).convert()


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

        self.interacoes = [
            # Máscara (faixa superior – centro)
            {
                "rect": pygame.Rect(630, 200, 120, 100),
                "tipo": "key",
                "categoria": "mascara"
            },

            # Armário (lado direito – área verde)
            {
                "rect": pygame.Rect(370, 650, 350, 150),
                "tipo": "armario1",
                "categoria": "armario",
                "recompensa": "noctis"
            },

            # Porta / saída (parte de baixo – maleta)
            {
                "rect": pygame.Rect(WIDTH - 90, 360, 120, 140),
                "tipo": "fase2 - 1",
                "categoria": "porta"
            },
        ]



        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT)
        )
        self.background_no_mask = pygame.transform.scale (
            self.background_no_mask, (WIDTH, HEIGHT)
        )
    def draw(self, screen):
        if self.player.temKey():
            self.background = self.background_no_mask

        screen.blit(self.background, (0, 0))

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
