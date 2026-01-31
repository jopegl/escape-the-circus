from player import Player
import pygame

class Level:
    def __init__(self, player):
        self.player = player
        self.walls = []
        self.interacoes = []

    def update(self):
        self.player.update(self.walls, self.interacoes)
    
    def draw(self, screen):
        screen.fill((0,0,0))
        self.player.draw(screen)
        for wall in self.walls:
            pygame.draw.rect(screen, (0, 200, 0), wall)

        