import random

class Computadora:
    def __init__(self, nombre="PC", vidas=5):
        self.nombre = nombre
        self.vidas = vidas

    def perder_vida(self):
        self.vidas -= 1

    def esta_vivo(self):
        return self.vidas > 0

    def elegir_opcion(self):
        return random.randint(1, 3)
