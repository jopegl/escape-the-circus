import pygame

class Player:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,32,32)
        self.speed = 4
    
    def update(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_a]: dx -= self.speed
        if keys[pygame.K_d]: dx += self.speed
        if keys[pygame.K_w]: dy -= self.speed
        if keys[pygame.K_s]: dy += self.speed

        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect)