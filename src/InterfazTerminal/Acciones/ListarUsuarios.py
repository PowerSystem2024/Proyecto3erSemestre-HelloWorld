from ..Accion import Accion
from ..utilidades import *


class ListarUsuarios(Accion):

    def __init__(self, nombre: str, cajero):
        super().__init__(nombre)
        self._cajero = cajero

    def ejecutar(self, menu):
        borrar_pantalla()
        self._cajero.mostrar_usuarios_registrados() # ToDo: Hay que implementar un metodo para poder ver el tiempo que se quiera y luego salir
        esperar_tiempo()
        borrar_pantalla()
        menu.set_indice_actual(0) # Te devuelve a la pantalla principal del menu o submenu
        return

    def obtener_nombre(self) -> str:
        return self._nombre
