from level import Level
import pygame
import os 
from settings import *

class Level2(Level):
    def __init__(self, player):
        super().__init__(player)

        mask_path = os.path.join('assets', 'backgrounds', 'lvl2', 'mascaranotis.png')

        self.mascara_mizu_img = pygame.image.load(mask_path).convert_alpha()

        self.mascara_mizu_img = pygame.transform.scale(
            self.mascara_mizu_img,
            (100, 100)
        )

        self.darkness = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.darkness.fill((0, 0, 0, 220))

        self.light_radius = 100
        self.light = pygame.Surface(
            (self.light_radius * 2, self.light_radius * 2),
            pygame.SRCALPHA
        )

        # Começa totalmente escuro
        self.light.fill((0, 0, 0, 255))

        # Desenha vários círculos, do maior pro menor
        for r in range(self.light_radius, 0, -3):
            alpha = int(255 * (r / self.light_radius))
            pygame.draw.circle(
                self.light,
                (0, 0, 0, alpha),
                (self.light_radius, self.light_radius),
                r
            )




        bg_path = os.path.join('assets', 'backgrounds','lvl2', 'BACKGROUND2.png')
        self.background = pygame.image.load(bg_path).convert()

        self.walls = [
            pygame.Rect(0, 0, WIDTH, 10), #cima 
            
            #esquerda
            pygame.Rect(0, 0, 120, 350),  
            pygame.Rect(0, 500, 120, 500),

            #direita
            pygame.Rect(WIDTH - 115, 0, 120, 350),  
            pygame.Rect(WIDTH - 115, 500, 120, 500),

            pygame.Rect(0, HEIGHT, WIDTH, 40), #baixo
        ]

        barra_path = os.path.join('assets', 'backgrounds', 'lvl2', 'BARRA.png')
        
        # Imagem Horizontal
        self.wall_img_h = pygame.image.load(barra_path).convert_alpha()
        self.wall_img_h = pygame.transform.scale(self.wall_img_h, (200, 10))
        # Imagem Vertical (rotacionada)
        self.wall_img_v = pygame.transform.rotate(self.wall_img_h, 90)
        self.wall_img_v = pygame.transform.scale(self.wall_img_v, (10, 200))

        # Lista para guardar apenas o visual do labirinto
        self.maze_sprites = []

        layout_labirinto = [
            (120, 480, 'V'),
            (120, 40, 'V'), 
            (120, 0, 'V'),  
            (120, 640, 'V'),
            (120, 760, 'V'),
            (120, 0, 'H'),  
            (400, 0, 'H'),  
            (360, 0, 'H'),  
            (320, 0, 'H'),  
            (640, 0, 'H'),  
            (600, 0, 'H'),  
            (680, 0, 'H'),  
            (880, 0, 'V'),  
            (880, 160, 'V'),
            (880, 480, 'V'),
            (880, 680, 'V'),
            (120, 760, 'V'),
            (120, 760, 'V'),
            (120, 480, 'H'),
            (240, 280, 'V'),
            (240, 160, 'H'),
            (360, 160, 'V'),
            (360, 360, 'H'),
            (480, 240, 'H'),
            (680, 40, 'V'),
            (680, 0, 'V'),
            (360, 80, 'V'),
            (240, 80, 'H'),
            (400, 160, 'H'),
            (400, 80, 'H'),
            (440, 320, 'V'),
            (440, 440, 'H'),
            (640, 440, 'V'),
            (520, 520, 'H'),
            (520, 520, 'V'),
            (200, 600, 'V'),
            (240, 600, 'H'),
            (200, 600, 'H'),
            (200, 680, 'H'),
            (240, 680, 'H'),
            (680, 720, 'H'),
            (800, 520, 'V'),
            (600, 440, 'H'),
            (760, 240, 'V'),
            (760, 480, 'H'),
        ]


        # Criar os objetos (física + visual)
        for x, y, orientacao in layout_labirinto:
            if orientacao == 'H':
                img = self.wall_img_h
                rect = pygame.Rect(x, y, 200, 10) # W=300, H=30
            else:
                img = self.wall_img_v
                rect = pygame.Rect(x, y, 10, 200) # W=30, H=300

            # Adiciona colisão física (Player usa isso)
            self.walls.append(rect)
            
            # Adiciona à lista de desenho (Imagem + Retângulo)
            self.maze_sprites.append((img, rect))

        self.interacoes = [
            {
                "rect": pygame.Rect(116, 744, 120, 100),
                "tipo": "mizu",
                "categoria": "mascara"
            },

            {
                "rect": pygame.Rect(0, 360, 20, 140),
                "tipo": "fase1",
                "categoria": "porta"
            },
            {
                "rect": pygame.Rect(1051, 428, 20, 300),
                "tipo": "fase3-1",
                "categoria": "porta"
            },
        ]

        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT)
        )

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        for img, rect in self.maze_sprites:
            screen.blit(img, rect.topleft)

        for wall in self.walls:
            eh_sprite = False
            for img, sprite_rect in self.maze_sprites:
                if wall == sprite_rect:
                    eh_sprite = True
                    break
            if not eh_sprite:
                surf = pygame.Surface((wall.width, wall.height), pygame.SRCALPHA)
                pygame.draw.rect(surf, (0, 200, 0, 100), surf.get_rect())
                screen.blit(surf, wall.topleft)

        for zona in self.interacoes:
            rect = zona["rect"]

            # Define o rect da máscara Mizu
            if zona["tipo"] == "mizu":
                self.mascara_mizu_rect = rect

                # Só desenha a máscara se o jogador ainda NÃO pegou
                if not self.player.temMizu():
                    screen.blit(self.mascara_mizu_img, self.mascara_mizu_rect.topleft)

            # Desenha zonas de interação (opcional)
            surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            pygame.draw.rect(surf, (0, 0, 200, 100), surf.get_rect())
            screen.blit(surf, rect.topleft)


        self.player.draw(screen)
        self.desenharEscuridao(screen)

    def desenharEscuridao(self, screen):

        if self.player.mascara_equipada == "noctis":
            darkness = self.darkness.copy()

            lx = self.player.rect.centerx - self.light_radius
            ly = self.player.rect.centery - self.light_radius

            darkness.blit(
                self.light,
                (lx, ly),
                special_flags=pygame.BLEND_RGBA_MIN
            )

            screen.blit(darkness, (0, 0))
        else:
            screen.blit(self.darkness, (0, 0))

