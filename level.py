from player import Player
import pygame

class Level:
    def __init__(self, player):
        self.player = player

    def update(self):
        self.player.update()
    
    def draw(self, screen):
        screen.fill((0,0,0))
        self.player.draw(screen)