import pygame

pygame.init()

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frames = [pygame.transform.scale(pygame.image.load("Assets/Nugget_222base-x-no_bg.png").convert_alpha(), (100, 100))]
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 100
        self.velocidad_x = 6
        self.velocidad_y = 0
        self.gravedad = 0.5