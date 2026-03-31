import pygame
from settings import AZUL

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto, color=None):
        super().__init__()
        if color is None:
            self.image = pygame.Surface((ancho, alto), pygame.SRCALPHA)
            self.image.fill((0, 0, 0, 0))
        else:
            self.image = pygame.Surface((ancho, alto))
            self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))