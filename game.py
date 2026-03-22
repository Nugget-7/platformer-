import pygame
from settings import ANCHO, ALTO, BLANCO, AZUL
from jugador import Jugador
from plataforma import Plataforma
import sys
from enemigo import Enemigo
import random

plataformas = pygame.sprite.Group()
suelo = Plataforma(0, 550, 800, 50)
plataformas.add(suelo)
plataformas.add(Plataforma(200, 375, 200, 20))

class Juego:
    def __init__(self):
        pygame.init()

        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("...")
        self.clock = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 36)
        self.jugador = Jugador()
        self.puntaje = 0
        self.enemigos = enemigos = pygame.sprite.Group()
        enemigo_1 = Enemigo()
        self.enemigos.add(enemigo_1)
        self.acelerador = 0
        self.doble = False

    def ejecutar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            teclas = pygame.key.get_pressed()
            puntos_ganados = self.jugador.update(self.enemigos)
            self.puntaje += puntos_ganados

            if teclas[pygame.K_LEFT] or teclas[pygame.K_a]: # si presiono </a...
                self.jugador.velocidad_x = 6
                self.jugador.rect.x -=self.jugador.velocidad_x
                if pygame.sprite.spritecollide(self.jugador, plataformas, False):
                    self.jugador.rect.x += self.jugador.velocidad_x

            if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: # si presiono >/d...
                self.jugador.velocidad_x = 6
                self.jugador.rect.x += self.jugador.velocidad_x
                if pygame.sprite.spritecollide(self.jugador, plataformas, False):
                    self.jugador.rect.x -= self.jugador.velocidad_x

            if teclas[pygame.K_UP] or teclas[pygame.K_w] or teclas[pygame.K_SPACE]:
                self.jugador.rect.y += 5
                colisiones = pygame.sprite.spritecollide(self.jugador, plataformas, False)
                self.jugador.rect.y -= 5
                if colisiones:
                    self.jugador.velocidad_y = -14

            self.jugador.velocidad_y += self.jugador.gravedad
            self.jugador.rect.y += self.jugador.velocidad_y

            colisiones = pygame.sprite.spritecollide(self.jugador, plataformas, False)

            for plataforma in colisiones:
                if self.jugador.velocidad_y > 0:
                    self.jugador.rect.bottom = plataforma.rect.top
                    self.jugador.velocidad_y = 0
                elif self.jugador.velocidad_y < 0:
                    self.jugador.rect.top = plataforma.rect.bottom
                    self.jugador.velocidad_y = 0
                break

            self.pantalla.fill(BLANCO)

            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            plataformas.draw(self.pantalla)
            self.enemigos.draw(self.pantalla)


            self.enemigos.update(plataformas)

            if len(self.enemigos) <= 0:
                enemigo_1 = Enemigo()
                self.enemigos.add(enemigo_1)
                if self.doble:
                    enemigo_2 = Enemigo()
                    self.enemigos.add(enemigo_2)
                for enemigo in self.enemigos:
                    if self.jugador.rect.x <= 650:
                        enemigo.rect.x = self.jugador.rect.x + 150
                    else:
                        enemigo.rect.x = self.juagdor.rect.x - 50
                    enemigo.rect.y = 400

            if puntos_ganados > 0:
                if len(self.enemigos) >= 2:
                    self.acelerador += 0.1
                else:
                    self.acelerador += 0.2
                for enemigo in self.enemigos:
                    enemigo.velocidad_x += self.acelerador
                if self.puntaje == 1500:
                    enemigo_2 = Enemigo()
                    self.acelerador = 0
                    enemigo_1.velocidad_x = 3
                    enemigo_2.velocidad_x = 3
                    self.enemigos.add(enemigo_2)
                    self.doble = True

            texto_puntaje = self.fuente.render(f"Puntaje: {self.puntaje}", True, (0, 0, 0))
            self.pantalla.blit(texto_puntaje, (10, 10))

            pygame.display.flip()
            self.clock.tick(60)