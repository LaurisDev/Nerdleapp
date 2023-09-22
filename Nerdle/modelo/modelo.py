from dataclasses import dataclass


@dataclass
class Jugador:
    nombre_jugador: str = ""
    correo_jugador: str = ""


class Nerdle:
    def __init__(self):
        self.nombre_jugador: str = ""
        self.correo_jugador: str = ""

    def registrar_nombre_jugador(self, nombre_jugador: str) -> str:
        self.nombre_jugador = nombre_jugador
        return self.nombre_jugador

    def registrar_correo_jugador(self, correo_jugador: str) -> str:
        self.correo_jugador = correo_jugador
        return self.correo_jugador

    def comprobar_ecuacion(self):
        pass

    def numero_intentos(self):
        pass

    def estado_juego(self):
        pass

    def anunciar_resultado(self):
        pass
