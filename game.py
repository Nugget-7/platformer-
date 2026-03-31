import pygame
from settings import ANCHO, ALTO, BLANCO, AZUL, VERDE
from jugador import Jugador
from plataforma import Plataforma
import sys
from enemigo import Enemigo
import random

plataformas = pygame.sprite.Group()
suelo = Plataforma(0, 550, 800, 50)
plataformas.add(suelo)
plataformas.add(Plataforma(200, 375, 200, 20, VERDE))

class Juego:
    def __init__(self):
        pygame.init()

        # fondo de pantalla:
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("...")
        self.clock = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 36)
        self.fuente_grande = pygame.font.Font(None, 72)
        self.fondo = pygame.image.load("Assets/Fondo.webp")
        self.fondo = pygame.transform.scale(self.fondo, (ANCHO, ALTO))
        self.jugador = Jugador()
        self.puntaje = 200
        self.estado = "jugando"
        self.enemigos = enemigos = pygame.sprite.Group()
        enemigo_1 = Enemigo()
        self.enemigos.add(enemigo_1)
        self.acelerador = 0
        self.doble = False
        self.puntajes = []
        self.puntaje_mas_alto = 0

    def ejecutar(self):
        while True:
            self.clock.tick(60)
            self.pantalla.blit(self.fondo, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            teclas = pygame.key.get_pressed()
            resultado = self.jugador.update(self.enemigos)
            self.puntaje += resultado["puntos"]
            if resultado["danio"]:
                self.puntaje -= 200
                self.jugador.rect.x = 200
                self.jugador.rect.y = 100
                self.jugador.velocidad_y = 0
                print("Oh no. Perdiste 200 puntos")

                if self.puntaje < 0:
                    self.estado = "game_over"

            self.puntajes.append(self.puntaje)

            for nuevo_puntaje in self.puntajes:
                if nuevo_puntaje > self.puntaje_mas_alto:
                    self.puntaje_mas_alto = nuevo_puntaje
            
            if self.estado == "game_over":
                self.mostrar_game_over()

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

            if resultado["puntos"] > 0:
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

    def mostrar_game_over(self):
        self.pantalla.fill((0, 0, 0))

        texto_game_over = self.fuente_grande.render("GAME OVER", True, (255, 255, 255))
        texto_puntaje = self.fuente.render(f"Tu puntaje: {self.puntaje}", True, (255, 255, 255))
        texto_puntaje_mas_alto = self.fuente_grande.render(f"Puntaje más alto: {self.puntaje_mas_alto}", True, (255, 255, 255))
        posicion_game_over = texto_game_over.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))
        posicion_puntaje = texto_puntaje.get_rect(center=(ANCHO // 2, ALTO // 2 - 10))
        posicion_puntaje_mas_alto = texto_puntaje_mas_alto.get_rect(center=(ANCHO // 2, ALTO // 2 - 175))
        self.pantalla.blit(texto_game_over, posicion_game_over)
        self.pantalla.blit(texto_puntaje, posicion_puntaje)
        self.pantalla.blit(texto_puntaje_mas_alto, posicion_puntaje_mas_alto)
        self.jugador.rect.x = -2000
        for enemigo in self.enemigos:
            enemigo.kill()
        for plataforma in plataformas:
            plataforma.kill()