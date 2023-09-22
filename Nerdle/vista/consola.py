import sys
from typing import Optional

from Nerdle.modelo.modelo import Nerdle


class UIConsola:
    def __init__(self):
        self.nerdle: Optional[Nerdle] = None
        self.opciones = {
            "1": self.ver_intrucciones,
            "2": self.iniciar_nuevo_juego,
            "0": self.salir
        }

    @staticmethod
    def mostrar_menu():
        titulo = "NERDLE"
        print(f"\n{titulo:_^30}")
        print("1. Ver instrucciones")
        print("2. Iniciar nuevo juego")
        print("3. Ver estadisticas")
        print("0.Salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        print("\nBIEVENID@ A NUESTRO JUEGO DE NERDLE")
        self.registrar_jugador()
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    @staticmethod
    def ver_intrucciones():
        titulo = "¿Cómo jugar?"
        print(f"\n{titulo:_^30}")
        print("Se debe adivnar la secuencia matemática, en un número limitado de intentos, que consta de números"
              "entre 0 y 9, operaciones matemáticas básicas y el signo de igualdad")


    def iniciar_nuevo_juego(self):
        pass

    @staticmethod
    def salir():
        print("\nGRACIAS POR JUGAR CON NOSOTROS. VUELVA PRONTO")
        sys.exit(0)

    def registrar_jugador(self):
        nombre: str = input("¿Cuál es tu nombre?: ")
        correo: str = input("¿Cuál es su correo electrónico?: ")
        self.nerdle = Nerdle()
        self.nerdle.registrar_nombre_jugador(nombre)
        self.nerdle.registrar_correo_jugador(correo)




