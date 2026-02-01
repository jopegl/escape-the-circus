from level import Level
import pygame
import os 
from settings import *

class ending(Level):
    def __init__(self, player):
        super().__init__(player)

        bg_path = os.path.join('assets', 'backgrounds','ending', 'ENDING.png')
        self.background = pygame.image.load(bg_path).convert()