class Jugador:
    def __init__(self, nombre, vidas=5):
        self.nombre = nombre
        self.vidas = vidas

    def perder_vida(self):
        self.vidas -= 1

    def esta_vivo(self):
        return self.vidas > 0