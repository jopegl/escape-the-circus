from level import Level
import pygame
import os 
from settings import *

class Level2(Level):
    def __init__(self, player):
        super().__init__(player)

        self.darkness = pygame.Surface((WIDTH, HEIGHT))
        self.darkness.fill((0, 0, 0))
        self.darkness.set_alpha(220)  # quão escuro

        self.light_radius = 120
        self.light = pygame.Surface(
            (self.light_radius * 2, self.light_radius * 2),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            self.light,
            (0, 0, 0, 0),
            (self.light_radius, self.light_radius),
            self.light_radius
        )


        bg_path = os.path.join('assets', 'backgrounds', 'BACKGROUND1MASK.png')
        self.background = pygame.image.load(bg_path).convert()
        background_no_mask_path = os.path.join('assets', 'backgrounds', 'BACKGROUND1.png')
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
                "tipo": "porta1",
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

        # desenha escuridão
        if self.player.mascara_equipada == "noctis":
            darkness = self.darkness.copy()

            lx = self.player.rect.centerx - self.light_radius
            ly = self.player.rect.centery - self.light_radius

            darkness.blit(
                self.light,
                (lx, ly),
                special_flags=pygame.BLEND_RGBA_SUB
            )

            screen.blit(darkness, (0, 0))
        else:
            screen.blit(self.darkness, (0, 0))

        # 🔥 player por último
        self.player.draw(screen)

