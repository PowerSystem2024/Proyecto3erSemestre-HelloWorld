from ..Accion import Accion
from ..utilidades import *


class ConsultarSaldo(Accion):

    def __init__(self, nombre: str, cajero):
        super().__init__(nombre)
        self._cajero = cajero

    def ejecutar(self, menu):
        usuario_actual = self._cajero.get_usuario_actual()
        borrar_pantalla()
        usuario_actual.consultar_saldo()
        esperar_tiempo()
        borrar_pantalla()
        menu.set_indice_actual(0) # Te devuelve a la pantalla principal del menu o submenu
        return

    def obtener_nombre(self) -> str:
        return self._nombre
