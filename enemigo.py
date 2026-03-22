import pygame

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frames = [pygame.transform.scale(pygame.image.load("Assets/big_mac_no_bg.png").convert_alpha(), (150, 100))]

        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 400

        self.velocidad_x = 3
        self.velocidad_y = 0
        self.gravedad = 0.5

    def update(self, plataformas):
        self.rect.x += self.velocidad_x
        
        self.velocidad_y += self.gravedad
        self.rect.y += self.velocidad_y

        if self.rect.left <= 0 or self.rect.right >= 800:
            self.velocidad_x -= (self.velocidad_x * 2)
            self.image = pygame.transform.flip(self.image, True, False)

        colisiones = pygame.sprite.spritecollide(self, plataformas, False)

        for plataforma in colisiones:
            if self.velocidad_y > 0:
                self.rect.bottom = plataforma.rect.top                    
                self.velocidad_y = 0
            elif self.velocidad_y < 0:
                self.rect.top = plataforma.rect.bottom
                self.velocidad_y = 0
            break