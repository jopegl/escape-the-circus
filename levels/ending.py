import pygame
import os 
from settings import *

class Ending:
    def __init__(self, screen):
        self.screen = screen
        bg_path = os.path.join('assets', 'backgrounds','ending', 'YOUWIN.png')
        self.background = pygame.image.load(bg_path).convert()

    def draw(self):
        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT)
        )
        self.screen.blit(self.background, (0, 0))

    def update(self):
        self.draw()