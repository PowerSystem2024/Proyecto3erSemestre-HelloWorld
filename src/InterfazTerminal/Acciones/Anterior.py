from ..Accion import Accion
from ..utilidades import borrar_pantalla

class Anterior(Accion):

    def __init__(self, nombre):
        super().__init__(nombre)

    def obtener_nombre(self):
        return self._nombre

    def ejecutar(self, menu):
        borrar_pantalla()
        if menu.get_indice_actual() > 0:
            menu.set_indice_actual(menu.get_indice_actual() - 1)
        return