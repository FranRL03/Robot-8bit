import random
import time

import pygame

from models.lake import Lake

lakes = [Lake(220, 100, 150, 150), Lake(520, 300, 150, 150)]


class Robot:
    def __init__(self):
        self.vida = 10
        self.traje_acuatico = False
        self.position = [0, 0]
        self.speed = 8
        self.size = [1,1]
        self.image = pygame.image.load("assets/robot.png")

# si choca con un muro se le resta 1 de vida
    def recibir_dano_muro(self):
        time.sleep(0.1)
        self.vida -= 1

# si lleva traje acuatico de vuelve un return vacio, es decir, None
# si no lleva el traje se le restara 3 de vida
    def recibir_dano_agua(self):
        if self.traje_acuatico:
            return
        self.vida -= 3

    def verificar_colision_agua(self):
        for lake in lakes:
            if (
                    lake.rect.x <= self.position[0] <= lake.rect.x + lake.rect.width and
                    lake.rect.y <= self.position[1] <= lake.rect.y + lake.rect.height
            ):
                self.recibir_dano_agua()

# la pocion que recoje solo puede curar de 1 a 5 puntos de vida
# y las curaciones recibidas no pueden pasar de los 10 puntos de vida
# (no se si este metodo funciona asi)
    def recoger_pocion(self):
        cantidad = random.randint(1, 5)
        self.vida = min(10, self.vida + cantidad)


# si el robot recoje el traje el valor del traje acuatico se establece a true
    def recoger_traje_acuatico(self):
        self.traje_acuatico = True

# si el robot pierde el traje el valor del traje acuatico de establece a false
    def perder_traje_acuatico(self):
        self.traje_acuatico = False

    def move_right (self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed