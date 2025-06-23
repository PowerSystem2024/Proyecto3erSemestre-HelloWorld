from ..Accion import Accion
from ..Menu import Menu
from ..utilidades import borrar_pantalla

class CrearSubMenu(Accion):

    def __init__(self, nombre, acciones_submenu):
        super().__init__(nombre)
        self._submenu = Menu(acciones_submenu)

    def ejecutar(self, menu):
        borrar_pantalla()
        self._submenu.crear_menu()
        return
