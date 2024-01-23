import random

import pygame

class Robot:
    def __init__(self):
        self.vida = 10
        self.traje_acuatico = False

# si choca con un muro se le resta 1 de vida
    def recibir_dano_muro(self):
        self.vida -= 1

# si lleva traje acuatico de vuelve un return vacio, es decir, None
# si no lleva el traje se le restara 3 de vida
    def recibir_dano_agua(self):
        if self.traje_acuatico:
            return
        self.vida -= 3

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
