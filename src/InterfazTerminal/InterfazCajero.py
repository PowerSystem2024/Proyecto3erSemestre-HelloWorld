from .ConfiguracionGrafica import *
from ..Acciones import ACCIONES, ACCIONES_MENU_TERMINAL
from .ConfiguracionMenuInterfazTerminal import MENU_TERMINAL
from ..Errores import ErrorInterfazTerminal
from ..RespuestaSemantica import RespuestaSemantica

#Todo: Cambiar Tipo de Error desde ErrorInterfazTerminal a ErrorInterfazCajero

class InterfazCajero:

    def __init__(self, nombre_menu: str = "menu_entrada"):
        self._nombre_menu_actual = nombre_menu
        self._acciones = self._obtener_configuracion_menu(nombre_menu)
        self._indice_actual = 0
        self._historial_menu = []  # Guarda tuplas: (nombre_menu, indice_actual)

        self._validar_estructura_acciones(self._acciones)
        self._validar_limite_opciones_visibles(self._acciones)
        self._validar_acciones(self._acciones)
        self._validar_constantes_menu() #Todo: Llevar validacion de configuración grafica terminal a Renderizador Terminal


    def _obtener_configuracion_menu(self, nombre_menu: str) -> list[list[str]]:
        configuracion_menu = MENU_TERMINAL.get(nombre_menu)
        if not configuracion_menu or not isinstance(configuracion_menu, list):
            raise ErrorInterfazTerminal("menu_no_definido", nombre_menu=nombre_menu)
        return configuracion_menu

    def _validar_estructura_acciones(self, acciones):
        if not all(isinstance(grupo_acciones, list) for grupo_acciones in acciones):
            raise ErrorInterfazTerminal("estructura_invalida_menu")

    def _validar_limite_opciones_visibles(self, acciones):
        for grupo_acciones in acciones:
            if len(grupo_acciones) > MAX_OPCIONES_VISIBLES:
                raise ErrorInterfazTerminal("maximo_opciones_excedido", MAX_OPCIONES_VISIBLES=MAX_OPCIONES_VISIBLES)
            elif len(grupo_acciones) < 1:
                raise ErrorInterfazTerminal("grupo_acciones_vacio")


    def _validar_acciones(self, acciones):
        for grupo_acciones in acciones:
            for tipo_accion in grupo_acciones:

                if not isinstance(tipo_accion, str):
                    raise ErrorInterfazTerminal("tipo_accion_no_es_cadena")

                if tipo_accion.startswith("menu:"):
                    clave = tipo_accion.removeprefix("menu:")

                    if clave in ACCIONES_MENU_TERMINAL:
                        datos = ACCIONES_MENU_TERMINAL[clave]
                        if "nombre" not in datos or not datos["nombre"]:
                            raise ErrorInterfazTerminal("accion_menu_sin_nombre", tipo_accion=tipo_accion)
                        if "funcion" not in datos or not callable(datos["funcion"]):
                            raise ErrorInterfazTerminal("accion_menu_sin_funcion", tipo_accion=tipo_accion)

                    elif clave in MENU_TERMINAL:
                        configuracion_menu = MENU_TERMINAL[clave]
                        if not isinstance(configuracion_menu, list) or not all(isinstance(grupo, list) for grupo in configuracion_menu):
                            raise ErrorInterfazTerminal("configuracion_menu_invalida", nombre_menu=clave)
                        # Validación recursiva de acciones del submenu
                        self._validar_acciones(configuracion_menu)

                    else:
                        raise ErrorInterfazTerminal("accion_menu_no_definida", tipo_accion=tipo_accion)

                elif tipo_accion in ACCIONES:
                    datos = ACCIONES[tipo_accion]
                    if "nombre" not in datos or not datos["nombre"]:
                        raise ErrorInterfazTerminal("accion_sin_nombre", tipo_accion=tipo_accion)
                    if "funcion" not in datos or not callable(datos["funcion"]):
                        raise ErrorInterfazTerminal("accion_sin_funcion", tipo_accion=tipo_accion)

                else:
                    raise ErrorInterfazTerminal("accion_no_definida", tipo_accion=tipo_accion)



    def menu_abrir(self, nombre_menu_submenu: str):
        """
        Abre un submenú, registrando el contexto actual en el historial
        y cargando la configuración del nuevo menú.
        """
        try:
            self._historial_menu.append((self._nombre_menu_actual, self._indice_actual))
            self._nombre_menu_actual = nombre_menu_submenu
            self._acciones = self._obtener_configuracion_menu(nombre_menu_submenu)
            self._indice_actual = 0
            return RespuestaSemantica("menu_abrir").con_exito({
                "menu_abierto": nombre_menu_submenu
            }).obtener_diccionario()
        except Exception:
            return RespuestaSemantica("menu_abrir").con_error("menu_no_definido").obtener_diccionario()

    def menu_volver(self):
        if self._historial_menu:
            nombre_menu_anterior, indice_anterior = self._historial_menu.pop()
            self._nombre_menu_actual = nombre_menu_anterior
            self._acciones = self._obtener_configuracion_menu(nombre_menu_anterior)
            self._indice_actual = indice_anterior
            return RespuestaSemantica("menu_volver").con_exito().obtener_diccionario()
        
        return RespuestaSemantica("menu_volver").con_error("sin_menu_anterior").obtener_diccionario()



    def menu_anterior(self):
        """
        Disminuye el índice actual del grupo de acciones, si es posible.
        """
        indice_anterior = self.obtener_indice_actual()
        nuevo_indice = max(0, indice_anterior - 1)
        self.set_indice_actual(nuevo_indice)

        return RespuestaSemantica("menu_anterior").con_exito({
            "indice_anterior": indice_anterior,
            "nuevo_indice": nuevo_indice
        }).obtener_diccionario()


    def menu_siguiente(self):
        indice_anterior = self.obtener_indice_actual()
        max_index = len(self._acciones) - 1
        nuevo_indice = min(max_index, indice_anterior + 1)
        self.set_indice_actual(nuevo_indice)
        return RespuestaSemantica("menu_siguiente").con_exito({
            "indice_anterior": indice_anterior,
            "nuevo_indice": nuevo_indice
        }).obtener_diccionario()



    def obtener_indice_actual(self):
        return self._indice_actual

    def set_indice_actual(self, nuevo_indice):
        self._indice_actual = nuevo_indice

    def get_acciones(self):
        return self._acciones

    #ToDo: Convertir Errores al tipo ErrorInterfazTerminal, llevar a Renderizador Terminal
    def _validar_constantes_menu(self):
        if MAX_OPCIONES_VISIBLES < 1:
            raise ValueError("MAX_OPCIONES_VISIBLES debe ser como mínimo igual a 1.")
        if MAX_OPCIONES_VISIBLES % 2 != 0:
            raise ValueError("MAX_OPCIONES_VISIBLES debe ser un número par.")
        if MAX_OPCIONES_VISIBLES // 2 != NUMERO_FILAS_MENU:
            raise ValueError("MAX_OPCIONES_VISIBLES debe ser el doble de NUMERO_FILAS_MENU.")
        
    def elegir_opcion(self, grupo_acciones: list[str], entrada: str) -> dict:
        tipo_respuesta = "elegir_opcion"
        respuesta = RespuestaSemantica(tipo_respuesta)

        try:
            opcion = int(entrada)
            if 1 <= opcion <= len(grupo_acciones):
                return respuesta.con_exito({
                    "indice_opcion": opcion - 1,
                    "tipo_accion": grupo_acciones[opcion - 1]
                }).obtener_diccionario()
            else:
                return respuesta.con_error("fuera_de_rango").obtener_diccionario()
        except ValueError:
            return respuesta.con_error("entrada_no_numerica").obtener_diccionario()


    def siguiente_campo_de_entrada(self, definicion_campos, tipo_accion, iterador) -> dict:
        respuesta = RespuestaSemantica(tipo_respuesta=tipo_accion)
        try:
            campo = next(iterador)
        except StopIteration:
            return respuesta.con_exito({"completado": True}).obtener_diccionario()

        # Aquí no se solicita la entrada directamente
        return respuesta.con_exito({
            "campo_actual": campo,
            "mensaje": definicion_campos[campo]["mensaje"],
            "completado": False
        }).obtener_diccionario()



    def obtener_grupo_acciones_actual(self):
        return self._acciones[self.obtener_indice_actual()]


    def obtener_indice_actual(self):
        return self._indice_actual