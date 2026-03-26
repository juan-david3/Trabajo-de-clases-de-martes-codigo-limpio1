from Jugador import Jugador
from Computadora import Computadora
from Reglas import Reglas
import Utilidades

class JuegoPiedraPapelTijera:
    def __init__(self):
        self.usuario = Jugador("Usuario")
        self.pc = Computadora()

    def jugar(self):
        print("=== JUEGO PIEDRA, PAPEL O TIJERA ===")
        print("Empiezan con 5 vidas cada uno. ¡Pierde una vida quien pierda la ronda!\n")

        while self.usuario.esta_vivo() and self.pc.esta_vivo():
            print(f"Vidas -> Usuario: {self.usuario.vidas} | PC: {self.pc.vidas}")

            opcion_usuario = Utilidades.Utilidades.obtener_opcion_usuario()
            opcion_pc = self.pc.elegir_opcion()

            nombre_usuario = Reglas.obtener_nombre_opcion(opcion_usuario)
            nombre_pc = Reglas.obtener_nombre_opcion(opcion_pc)

            print(f"Tú elegiste: {nombre_usuario}")
            print(f"La PC eligió: {nombre_pc}")

            ganador = Reglas.resultado(opcion_usuario, opcion_pc)

            if ganador == "empate":
                print("Resultado de la ronda: ¡Empate!\n")
            elif ganador == "usuario":
                self.pc.perder_vida()
                print("Resultado de la ronda: ¡Ganaste esta ronda!\n")
            else:
                self.usuario.perder_vida()
                print("Resultado de la ronda: La PC gana esta ronda.\n")

        self.mostrar_resultado_final()

    def mostrar_resultado_final(self):
        print("=== FIN DEL JUEGO ===")
        if self.usuario.esta_vivo():
            print("¡Felicidades! Ganaste el juego.")
        else:
            print("La PC ganó el juego. ¡Inténtalo de nuevo!")
