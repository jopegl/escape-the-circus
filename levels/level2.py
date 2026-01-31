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
        # Imagem Vertical (rotacionada)
        self.wall_img_v = pygame.transform.rotate(self.wall_img_h, 90)

        # Lista para guardar apenas o visual do labirinto
        self.maze_sprites = []

        # ==========================================================
        # 2. O QUE FALTAVA: DEFINIR O LABIRINTO
        # ==========================================================
        # ==========================================================
        # DEFINIÇÃO DE UM LABIRINTO REAL (Ziguezague)
        # ==========================================================
        # ==========================================================
        # LABIRINTO DENSO (14 PAREDES)
        # ==========================================================
        layout_labirinto = [

            # ===============================
            # ZONA ESQUERDA — INÍCIO
            # ===============================

            # Entrada bloqueada → força descer
            (220, 50, 'V'),

            # Cria corredor inicial
            (80, 380, 'H'),
            (380, 150, 'V'),

            # Beco sem saída à esquerda
            (120, 200, 'V'),
            (120, 300, 'H'),

            # ===============================
            # ZONA CENTRAL — MÁSCARA
            # ===============================

            # Caixa da máscara (proteção em volta)
            (500, 120, 'H'),   # teto
            (480, 320, 'H'),   # chão
            (550, 160, 'V'),   # esquerda
            (700, 160, 'V'),   # direita

            # Entrada obrigatória por baixo
            (600, 360, 'H'),

            # Falso caminho acima da máscara
            (600, 60, 'H'),
            (750, 60, 'V'),

            # ===============================
            # ZONA INFERIOR — ESGOTO
            # ===============================

            # Corredor apertado
            (150, 550, 'H'),
            (400, 500, 'V'),

            # Labirinto em zigue-zague
            (300, 720, 'H'),
            (500, 650, 'V'),
            (350, 650, 'H'),
            (350, 600, 'V'),

            # Beco sem saída inferior
            (200, 680, 'V'),
            (200, 760, 'H'),

            # ===============================
            # ZONA DIREITA — SAÍDA
            # ===============================

            # Bloqueia acesso direto por cima
            (850, 50, 'V'),
            (820, 250, 'H'),

            # Proteção inferior da porta
            (880, 500, 'V'),
            (650, 600, 'H'),

            # Curva final obrigatória
            (720, 650, 'V'),
            (760, 700, 'H'),

            # Último desvio antes da porta
            (820, 620, 'V'),
        ]


        # Criar os objetos (física + visual)
        for x, y, orientacao in layout_labirinto:
            if orientacao == 'H':
                img = self.wall_img_h
                rect = pygame.Rect(x, y, 300, 30) # W=300, H=30
            else:
                img = self.wall_img_v
                rect = pygame.Rect(x, y, 30, 300) # W=30, H=300

            # Adiciona colisão física (Player usa isso)
            self.walls.append(rect)
            
            # Adiciona à lista de desenho (Imagem + Retângulo)
            self.maze_sprites.append((img, rect))

        self.interacoes = [
            # Máscara (faixa superior – centro)
            {
                "rect": pygame.Rect(630, 200, 120, 100),
                "tipo": "key",
                "categoria": "mascara"
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

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        # --- 1. O QUE FALTOU: Desenhar as paredes bonitas (Sprites) ---
        for img, rect in self.maze_sprites:
            screen.blit(img, rect.topleft)

        # --- 2. Desenhar as bordas invisíveis (Debug Verde) ---
        # Aqui fazemos uma verificação: só desenha o quadrado verde 
        # se a parede NÃO for uma das paredes do labirinto (sprites).
        for wall in self.walls:
            eh_sprite = False
            # Procura se esse 'wall' existe na lista de sprites
            for img, sprite_rect in self.maze_sprites:
                if wall == sprite_rect:
                    eh_sprite = True
                    break
            
            # Se não é sprite (ou seja, é uma borda invisível), desenha o verde
            if not eh_sprite:
                surf = pygame.Surface((wall.width, wall.height), pygame.SRCALPHA)
                pygame.draw.rect(surf, (0, 200, 0, 100), surf.get_rect())
                screen.blit(surf, wall.topleft)

        # --- 3. Desenhar Interações ---
        for zona in self.interacoes:
            rect = zona["rect"]
            surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            pygame.draw.rect(surf, (0, 0, 200, 100), surf.get_rect())
            screen.blit(surf, rect.topleft)

        # desenha escuridão
        #if self.player.mascara_equipada == "noctis":
         #   darkness = self.darkness.copy()

          #  lx = self.player.rect.centerx - self.light_radius
           # ly = self.player.rect.centery - self.light_radius

            #darkness.blit(
              #  self.light,
             #   (lx, ly),
               # special_flags=pygame.BLEND_RGBA_SUB
            #)

            #screen.blit(darkness, (0, 0))
        #else:
         #   screen.blit(self.darkness, (0, 0))
        self.player.draw(screen)

