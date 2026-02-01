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
        self.overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.overlay.fill((10, 10, 20, 35))
        self.darkness = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.darkness.fill((0, 0, 0, 90))
        self.light_surf = pygame.Surface((500, 500), pygame.SRCALPHA)
        self.light_surf.fill((0, 0, 0, 255))
        self.luzes = [
            (300, 180, 150),
            (700, 500, 150),
        ]



        for r in range(150, 0, -3):
            alpha = int(255 * (r / 150))
            pygame.draw.circle(
                self.light_surf,
                (0, 0, 0, alpha),
                (150, 150),
                r
            )



        self.walls = [
            pygame.Rect(0, 40, WIDTH, 180), #cima 
            
            #esquerda
            pygame.Rect(0, 60, 120, 300),  
            pygame.Rect(0, 500, 120, 300),

            #direita
            pygame.Rect(WIDTH - 115, 60, 120, 300),  
            pygame.Rect(WIDTH - 115, 500, 120, 300),
            pygame.Rect(370, 720, 350, 150),

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
            pygame.draw.rect(surf, (0, 0, 0, 0), surf.get_rect())
            screen.blit(surf, wall.topleft)

        for zona in self.interacoes:
            rect = zona["rect"]
            surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            pygame.draw.rect(surf, (0, 0, 0, 0), surf.get_rect())
            screen.blit(surf, rect.topleft)
        self.player.draw(screen)
        dark = self.darkness.copy()

        for x, y, _ in self.luzes:
            dark.blit(
                self.light_surf,
                (x - 150, y - 150),
                special_flags=pygame.BLEND_RGBA_MIN
            )

        # desenha a escuridão final
        screen.blit(dark, (0, 0))
        screen.blit(self.overlay, (0, 0))

