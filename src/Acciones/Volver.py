from ..Accion import Accion
from ..utilidades import borrar_pantalla

class Volver(Accion):

    def __init__(self, nombre):
        super().__init__(nombre)

    def obtener_nombre(self):
        return self._nombre

    def ejecutar(self, menu):
        borrar_pantalla()
        return True
