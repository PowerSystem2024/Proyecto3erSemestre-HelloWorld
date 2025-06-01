from ..Accion import Accion
from ..utilidades import *


class CrearUsuario(Accion):

    def __init__(self, nombre: str, cajero):
        super().__init__(nombre)
        self._cajero = cajero

    def ejecutar(self, menu):
        borrar_pantalla()
        self._cajero.generar_usuario() 
        esperar_tiempo()
        borrar_pantalla()
        menu.set_indice_actual(0) # Te devuelve a la pantalla principal del menu o submenu
        return

