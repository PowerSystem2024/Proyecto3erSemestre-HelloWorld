from ..utilidades import *
from ..Menu import Menu
from .CrearSubMenu import CrearSubMenu

class IniciarSesion(CrearSubMenu):
    """Acción que crea un submenu menu principal en caso que logre autentificarse sino se vuelve a la pantalla principal del menu de entrada"""
    def __init__(self, nombre, acciones_submenu, cajero, acciones_menu_secreto):
        super().__init__(nombre, acciones_submenu)
        self._cajero = cajero
        self._menu_secreto = Menu(acciones_menu_secreto)

    def ejecutar(self, menu):
        borrar_pantalla()
        if self._cajero.iniciar_sesion():  # Si se logra autentificar el usuario, se entra al menu principal
            if (self._cajero.get_usuario_actual().get_nombre() == 'admin'):
                self._menu_secreto.crear_menu()
                borrar_pantalla()
                return
            self._submenu.crear_menu()
        else:
            menu.set_indice_actual(0) # Te devuelve a la pantalla principal del menu o submenu
        borrar_pantalla()
        return
