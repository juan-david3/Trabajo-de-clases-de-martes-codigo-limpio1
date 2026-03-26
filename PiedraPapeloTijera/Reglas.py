class Reglas:
    opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}

    @staticmethod
    def obtener_nombre_opcion(opcion):
        return Reglas.opciones[opcion]

    @staticmethod
    def resultado(opcion_usuario, opcion_pc):
        if opcion_usuario == opcion_pc:
            return "empate"
        if (
            (opcion_usuario == 1 and opcion_pc == 3)
            or (opcion_usuario == 2 and opcion_pc == 1)
            or (opcion_usuario == 3 and opcion_pc == 2)
        ):
            return "usuario"
        return "pc"
