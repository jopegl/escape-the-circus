from level import Level
import pygame

class Level1(Level):
    def __init__(self, player):
        super().__init__(player)
        
        self.walls = [
            pygame.Rect(200, 200, 300, 20),
        ]