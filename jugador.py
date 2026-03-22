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

    def update(self, enemigos):
        colisiones_enemigos = pygame.sprite.spritecollide(self, enemigos, False)
        puntos_ganados = 0
        for enemigo in colisiones_enemigos:
            if self.velocidad_y > 0 and self.rect.bottom <= enemigo.rect.top + 20:
                puntos_ganados += 100
                enemigo.kill()
            if self.rect.right <= enemigo.rect.left + 25 or self.rect.left >= enemigo.rect.right - 25:
                puntos_ganados -= 200
                self.rect.x = 200
                self.rect.y = 100
        return puntos_ganados