import pygame
import os 
from settings import *
from level import Level
import time

class Ending:
    def __init__(self):
        bg_path = os.path.join('assets', 'backgrounds','ending', 'YOUWIN.png')
        self.background = pygame.image.load(bg_path).convert()
        self.finished = False

    def draw(self, screen):
        bg = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        screen.blit(bg, (0, 0))

    def update(self):
        if not self.finished:
            time.sleep(10)
            self.finished = True
