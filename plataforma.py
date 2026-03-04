import pygame
from settings import AZUL

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect(topleft=(x, y))