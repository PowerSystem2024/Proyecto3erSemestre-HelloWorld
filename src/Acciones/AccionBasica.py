from ..Accion import Accion
from ..utilidades import *

class AccionBasica(Accion):
    """
    Representa una acción básica del cajero que contiene un nombre identificador.

    Atributos:
        _nombre (str): Nombre de la acción.

    Métodos:
        obtener_nombre(): Retorna el nombre de la acción.
    """

    def __init__(self, nombre: str):
        super().__init__(nombre)

    def ejecutar(self, menu):
        borrar_pantalla()
        escribir_con_retraso(f"Soy la acción {self.obtener_nombre()} muajajaja.")
        esperar_tiempo()
        borrar_pantalla()
        menu.set_indice_actual(0) # Te devuelve a la pantalla principal del menu o submenu
        return

    def obtener_nombre(self) -> str:
        return self._nombre
