from ..Accion import Accion
from ..utilidades import *

class Salir(Accion):

    def __init__(self, nombre):
        super().__init__(nombre)

    def ejecutar(self, menu):
        borrar_pantalla()
        imprimir_con_delay("Cerrando Sesión...") # ToDo: Arreglar Esteticamente
        borrar_pantalla()
        return True  # Señal para salir del bucle del submenu al menu anterior
