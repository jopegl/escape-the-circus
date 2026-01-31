import pygame
from settings import *

class Player:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,32,32)
        self.speed = PLAYER_SPEED
        self.lista_mascaras = ["key", "noctis", "mizu"]
        self.mascaras_coletadas = {
            "key": False,
            "noctis": False,
            "mizu": False
        }
        self.mascara_equipada = None
        self.proxima_fase = None
    
    def update(self, walls, interacoes):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_a]: dx -= self.speed
        if keys[pygame.K_d]: dx += self.speed
        if keys[pygame.K_w]: dy -= self.speed
        if keys[pygame.K_s]: dy += self.speed

        self.rect.x += dx
        self._collide(dx, 0, walls)

        self.rect.y += dy
        self._collide(0, dy, walls)

        self.trocarMascara()
        self.manipularInteracoes(interacoes)



    def _collide(self,dx,dy,walls):
        for wall in walls:
            if self.rect.colliderect(wall):
                if dx > 0:   # indo pra direita
                    self.rect.right = wall.left
                if dx < 0:   # esquerda
                    self.rect.left = wall.right
                if dy > 0:   # descendo
                    self.rect.bottom = wall.top
                if dy < 0:   # subindo
                    self.rect.top = wall.bottom


    def manipularInteracoes(self, interacoes):
        keys = pygame.key.get_pressed()
    
        for zona in interacoes:
            if self.rect.colliderect(zona["rect"]):
                
                if zona.get("categoria") == "mascara":
                    if keys[pygame.K_e]:
                        tipo = zona["tipo"]
                        if not self.mascaras_coletadas[tipo]:
                            self.mascaras_coletadas[tipo] = True
                            print(f"Você pegou a máscara {tipo}!")
                            interacoes.remove(zona)
                            break  # pega apenas uma por aperto
                elif zona.get('categoria') == 'armario':
                    if keys[pygame.K_e]:
                        if self.temKey() and self.mascara_equipada == 'key':
                            self.mascaras_coletadas[zona.get('recompensa')] = True
                            print("Você abriu o armário!")
                            interacoes.remove(zona)
                elif zona.get("categoria") == "porta":
                    self.proxima_fase = zona["tipo"]
                    print(f"Entrando na {zona['tipo']}...")


                

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect)

    def trocarMascara(self):
        keys = pygame.key.get_pressed()

        for i, nome in enumerate(self.lista_mascaras):
            if keys[pygame.K_1 + i]:
                if self.mascaras_coletadas[nome]:
                    self.mascara_equipada = nome
                    print(f"Máscara equipada: {nome}")
        
        if keys[pygame.K_4]:
            self.mascara_equipada = None


    
    def temKey(self):
        return self.mascaras_coletadas['key']
    def temNoctis(self):
        return self.mascaras_coletadas['noctis']
    def temMizu(self):
        return self.mascaras_coletadas['mizu']
    