import pygame
import os
from settings import *

def load_scaled(path, scale):
    img = pygame.image.load(path).convert_alpha()
    w, h = img.get_size()
    return pygame.transform.scale(
        img,
        (int(w * scale), int(h * scale))
    )

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.collect_sound_path = os.path.join('assets', 'sounds', 'collect.mp3')
        self.walk_sound_path = os.path.join('assets', 'sounds', 'steps.mp3')

        self.collect_sound = pygame.mixer.Sound(self.collect_sound_path)
        self.walk_sound = pygame.mixer.Sound(self.walk_sound_path)



        self.collect_sound.set_volume(0.7)
        self.walk_sound.set_volume(0.4)

        self.walk_channel = pygame.mixer.Channel(1)

        self.ganhou = False

        self.speed = PLAYER_SPEED
        self.lista_mascaras = ["key", "noctis", "mizu"]
        self.mascaras_coletadas = {
            "key": False,
            "noctis": False,
            "mizu": False
        }
        self.mascara_equipada = None
        self.proxima_fase = None

        base_path = os.path.join("assets", "sprites", "normal")
        mask_path = os.path.join("assets", "sprites", "masked")

        self.animations = {
            'down': [
                load_scaled(os.path.join(base_path, "frente", "frente.png"), SPRITE_SCALE),
                load_scaled(os.path.join(base_path, "frente", "frentepe1.png"), SPRITE_SCALE),
                load_scaled(os.path.join(base_path, "frente", "frentepe2.png"), SPRITE_SCALE)
            ],
            'down_1': [
                load_scaled(os.path.join(mask_path, "frente", "frente2mask1.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "frente", "frente1mask1.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "frente", "frente3mask1.png"), SPRITE_SCALE)
            ],
            'down_2': [
                load_scaled(os.path.join(mask_path, "frente", "frente2mask2.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "frente", "frente1mask2.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "frente", "frente3mask2.png"), SPRITE_SCALE)
            ],
            'down_3': [
                load_scaled(os.path.join(mask_path, "frente", "frente2mask3.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "frente", "frente1mask3.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "frente", "frente3mask3.png"), SPRITE_SCALE)
            ],
            'up': [
                load_scaled(os.path.join(base_path, "costas", "costa.png"), SPRITE_SCALE),
                load_scaled(os.path.join(base_path, "costas", "costaspe1.png"), SPRITE_SCALE),
                load_scaled(os.path.join(base_path, "costas", "costaspe2.png"), SPRITE_SCALE)
            ],
            'right': [
                load_scaled(os.path.join(base_path, "direita", "direita.png"), SPRITE_SCALE),
                load_scaled(os.path.join(base_path, "direita", "direitape1.png"), SPRITE_SCALE),
                load_scaled(os.path.join(base_path, "direita", "direitape2.png"), SPRITE_SCALE)
            ],
            'right_1': [
                load_scaled(os.path.join(mask_path, "direita", "direita2mask1.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "direita", "direita1mask1.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "direita", "direita3mask1.png"), SPRITE_SCALE)
            ],
            'right_2': [
                load_scaled(os.path.join(mask_path, "direita", "direita2mask2.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "direita", "direita1mask2.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "direita", "direita3mask2.png"), SPRITE_SCALE)
            ],
            'right_3': [
                load_scaled(os.path.join(mask_path, "direita", "direita2mask3.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "direita", "direita1mask3.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "direita", "direita3mask3.png"), SPRITE_SCALE)
            ],
            'left': [
                load_scaled(os.path.join(base_path, "esquerda", "esquerda.png"), SPRITE_SCALE),
                load_scaled(os.path.join(base_path, "esquerda", "esqpe1.png"), SPRITE_SCALE),
                load_scaled(os.path.join(base_path, "esquerda", "esqpe2.png"), SPRITE_SCALE)
            ],
            'left_1': [
                load_scaled(os.path.join(mask_path, "esquerda", "esq2mask1.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "esquerda", "esq1mask1.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "esquerda", "esq3mask1.png"), SPRITE_SCALE)
            ],
            'left_2': [
                load_scaled(os.path.join(mask_path, "esquerda", "esq2mask2.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "esquerda", "esq1mask2.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "esquerda", "esq3mask2.png"), SPRITE_SCALE)
            ],
            'left_3': [
                load_scaled(os.path.join(mask_path, "esquerda", "esq2mask3.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "esquerda", "esq1mask3.png"), SPRITE_SCALE),
                load_scaled(os.path.join(mask_path, "esquerda", "esq3mask3.png"), SPRITE_SCALE)
            ]
        }

        self.status = 'down';
        self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]
        self.rect = self.image.get_rect(topleft=(x, y))

        # Hitbox só do tronco pra baixo
        self.hitbox = pygame.Rect(
            self.rect.x + self.rect.width * 0.2,   # margem esquerda
            self.rect.y + self.rect.height * 0.45,  # começa abaixo da cabeça
            self.rect.width * 0.6,                  # mais estreita
            self.rect.height * 0.5                  # só parte inferior
        )

    def update(self, walls, interacoes):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_w]:
            dy = -self.speed
            self.status = 'up'

        elif keys[pygame.K_s]: 
            dy = self.speed
            if self.mascara_equipada == 'key':
                self.status = 'down_1'
            elif self.mascara_equipada == 'noctis':
                self.status = 'down_2'
            elif self.mascara_equipada == 'mizu':
                self.status = 'down_3'
            else:
                self.status = 'down'

        if keys[pygame.K_a]: 
            dx = -self.speed
            if self.mascara_equipada == 'key':
                self.status = 'left_1'
            elif self.mascara_equipada == 'noctis':
                self.status = 'left_2'
            elif self.mascara_equipada == 'mizu':
                self.status = 'left_3'
            else:
                self.status = 'left'

        elif keys[pygame.K_d]: 
            dx = self.speed
            if self.mascara_equipada == 'key':
                self.status = 'right_1'
            elif self.mascara_equipada == 'noctis':
                self.status = 'right_2'
            elif self.mascara_equipada == 'mizu':
                self.status = 'right_3'
            else:
                self.status = 'right'

        self.hitbox.x += dx
        self._collide(dx, 0, walls)

        self.hitbox.y += dy
        self._collide(0, dy, walls)

        self.rect.midbottom = self.hitbox.midbottom

        self.trocarMascara()
        self.manipularInteracoes(interacoes)

        self.animate(dx != 0 or dy != 0)
        is_moving = dx != 0 or dy != 0

        if is_moving:
            if not self.walk_channel.get_busy():
                self.walk_channel.play(self.walk_sound, loops=-1)
        else:
            self.walk_channel.stop()


    def animate(self, is_moving):
        if is_moving:
            self.frame_index += 0.1  # Avança a animação devagar
            if self.frame_index >= len(self.animations[self.status]):
                    self.frame_index = 0
        else:
            self.frame_index = 0 # Volta para o frame inicial se parar
        
        self.image = self.animations[self.status][int(self.frame_index)]

    def _collide(self, dx, dy, walls):
        for wall in walls:
            if self.hitbox.colliderect(wall):
                if dx > 0:
                    self.hitbox.right = wall.left
                if dx < 0:
                    self.hitbox.left = wall.right
                if dy > 0:
                    self.hitbox.bottom = wall.top
                if dy < 0:
                    self.hitbox.top = wall.bottom


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def manipularInteracoes(self, interacoes):
        keys = pygame.key.get_pressed()
    
        for zona in interacoes:
            if self.rect.colliderect(zona["rect"]):
                
                if zona.get("categoria") == "mascara":
                    if keys[pygame.K_e]:
                        tipo = zona["tipo"]
                        if not self.mascaras_coletadas[tipo]:
                            self.mascaras_coletadas[tipo] = True
                            self.collect_sound.play()
                            print(f"Você pegou a máscara {tipo}!")
                            interacoes.remove(zona)
                            break  # pega apenas uma por aperto
                elif zona.get('categoria') == 'armario':
                    if keys[pygame.K_e]:
                        if self.temKey() and self.mascara_equipada == 'key':
                            self.mascaras_coletadas[zona.get('recompensa')] = True
                            self.collect_sound.play()
                            print("Você abriu o armário!")
                            interacoes.remove(zona)
                elif zona.get("categoria") == "porta":
                    self.proxima_fase = zona["tipo"]
                    print(f"Entrando na {zona['tipo']}...")
                elif zona.get('categoria') == 'final':
                    if keys[pygame.K_e]:
                        if self.temKey() and self.mascara_equipada == 'key':
                            self.ganhou = True
 

    def trocarMascara(self):
        keys = pygame.key.get_pressed()
        mascara_anterior = self.mascara_equipada

        for i, nome in enumerate(self.lista_mascaras):
            if keys[pygame.K_1 + i]:
                if self.mascaras_coletadas[nome]:
                    self.mascara_equipada = nome
                    print(f"Máscara equipada: {nome}")
        
        if keys[pygame.K_4]:
            self.mascara_equipada = None

        if self.mascara_equipada != mascara_anterior:
            if 'down' in self.status:
                self.status = 'down' if not self.mascara_equipada else f'down_{self.lista_mascaras.index(self.mascara_equipada)+1}'
            elif 'up' in self.status:
                self.status = 'up'
            elif 'left' in self.status:
                self.status = 'left' if not self.mascara_equipada else f'left_{self.lista_mascaras.index(self.mascara_equipada)+1}'
            elif 'right' in self.status:
                self.status = 'right' if not self.mascara_equipada else f'right_{self.lista_mascaras.index(self.mascara_equipada)+1}'


    
    def temKey(self):
        return self.mascaras_coletadas['key']
    def temNoctis(self):
        return self.mascaras_coletadas['noctis']
    def temMizu(self):
        return self.mascaras_coletadas['mizu']
    

