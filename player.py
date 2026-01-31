import pygame

class Player:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,32,32)
        self.speed = 4
    
    def update(self, walls):
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


    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect)