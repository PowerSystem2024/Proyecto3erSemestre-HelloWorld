from ..Accion import Accion
from ..utilidades import *

class TerminarPrograma(Accion):
    def __init__(self, nombre: str, cajero):
        super().__init__(nombre)
        self._cajero = cajero

    def ejecutar(self, menu):
        borrar_pantalla()
        self._cajero.terminar_programa()
        return
