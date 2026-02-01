from level import Level
import pygame
import os 
from settings import *

class Level3_1(Level):
    def __init__(self, player):
        super().__init__(player)

        bg_path = os.path.join('assets', 'backgrounds','lvl3', 'PREBACKGROUND3.png')
        self.background = pygame.image.load(bg_path).convert()
        self.bloqueador = pygame.Rect(420, 0, 30, HEIGHT)
        self.desenhar_bloqueador = True
        self.mensagem_bloqueador = "Essa piscina é muito funda"
        self.mostrar_mensagem = False
        self.timer_mensagem = 0 


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
            {
                "rect": pygame.Rect(0, 360, 20, 140),
                "tipo": "fase2-2",
                "categoria": "porta"
            },

            {
                "rect": pygame.Rect(450, 0, 20, HEIGHT),
                "tipo": "fase3-2",
                "categoria": "porta"
            },
        ]



        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT)
        )

        self.font = pygame.font.Font(None, 30)

    def update(self):
        super().update()
        if self.bloqueador.colliderect(self.player.rect) and self.player.mascara_equipada != 'mizu':
            if not self.mostrar_mensagem:
                self.mostrar_mensagem = True
                self.timer_mensagem = 120  

        if self.mostrar_mensagem:
            self.timer_mensagem -= 1
            if self.timer_mensagem <= 0:
                self.mostrar_mensagem = False

    def draw(self, screen):

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

        if hasattr(self, "bloqueador") and getattr(self, "desenhar_bloqueador", False):
            if self.player.mascara_equipada != 'mizu':
                surf = pygame.Surface((self.bloqueador.width, self.bloqueador.height), pygame.SRCALPHA)
                pygame.draw.rect(surf, (0, 0, 0, 0), surf.get_rect())  
                screen.blit(surf, self.bloqueador.topleft)

        self.player.draw(screen)

        if self.mostrar_mensagem:
            text_surf = self.font.render(self.mensagem_bloqueador, True, (255, 255, 255))  

            bg_surf = pygame.Surface((text_surf.get_width()+20, text_surf.get_height()+10), pygame.SRCALPHA)
            bg_surf.fill((0, 0, 0, 180))
            x = self.player.rect.centerx - text_surf.get_width()//2
            y = self.player.rect.top - text_surf.get_height() - 10  
            screen.blit(bg_surf, (x - 10, y - 5))
            screen.blit(text_surf, (x, y))


