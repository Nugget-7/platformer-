import pygame
from settings import ANCHO, ALTO, BLANCO, AZUL
from jugador import Jugador
from plataforma import Plataforma
import sys

plataformas = pygame.sprite.Group()
suelo = Plataforma(0, 550, 800, 50)
plataformas.add(suelo)
plataformas.add(Plataforma(200, 350, 200, 20))

class Juego:
    def __init__(self):
        pygame.init()

        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("...")
        self.clock = pygame.time.Clock()
        self.jugador = Jugador()

    def ejecutar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            teclas = pygame.key.get_pressed()

            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
                self.jugador.rect.x -= self.jugador.velocidad_x

            if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
                self.jugador.rect.x += self.jugador.velocidad_x

            if teclas[pygame.K_UP] or teclas[pygame.K_w] or teclas[pygame.K_SPACE]:
                self.jugador.rect.y += 5
                colisiones = pygame.sprite.spritecollide(self.jugador, plataformas, False)
                self.jugador.rect.y -= 5
                if colisiones:
                    self.jugador.velocidad_y = -12

            #if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
                #jugador.rect.y += jugador.velocidad_y

            self.jugador.velocidad_y += self.jugador.gravedad
            self.jugador.rect.y += self.jugador.velocidad_y

            colisiones = pygame.sprite.spritecollide(self.jugador, plataformas, False)

            for plataforma in colisiones:
                if self.jugador.velocidad_y > 0:
                    self.jugador.rect.bottom = plataforma.rect.top
                    self.jugador.velocidad_y = 0 #TODO para detenerlo
                elif self.jugador.velocidad_y < 0:
                    self.jugador.rect.top = plataforma.rect.bottom
                    self.jugador.velocidad_y = 0
                break

            self.pantalla.fill(BLANCO)

            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            plataformas.draw(self.pantalla)

            pygame.display.flip()
            self.clock.tick(60)