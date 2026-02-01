from player import Player
import pygame

class Level:
    def __init__(self, player):
        self.player = player
        self.walls = []
        self.interacoes = []

    def update(self):
        # Lista de colisão
        paredes_para_colisao = self.walls.copy()

        # Adiciona o bloqueador à colisão se existir e o jogador não tiver Mizu
        if hasattr(self, "bloqueador") and self.player.mascara_equipada != 'mizu':
            paredes_para_colisao.append(self.bloqueador)

        self.player.update(paredes_para_colisao, self.interacoes)
    
