from .RenderizadorInterfazTerminal import RenderizadorInterfazTerminal, LINEAS_RESPUESTA
from .InterfazCajero import InterfazCajero
from ..Acciones import ACCIONES, ACCIONES_MENU_TERMINAL
from .ConfiguracionMenuInterfazTerminal import ACCION_GENERADOR_SUBMENU, ENTRADAS_INTERFAZ
from ..ControladorCajero import ControladorCajero
from ..RespuestaSemantica import RespuestaSemantica


class ControladorInterfazTerminal:
    def __init__(self, interfaz: InterfazCajero, renderizador: RenderizadorInterfazTerminal):
        self._interfaz = interfaz
        self._renderizador = renderizador
        self._controlador_cajero = ControladorCajero()
        self._corriendo = True

        # Estado para recolección progresiva
        self._tipo_accion_actual = "elegir_opcion"
        self._definicion_campos_actual = ENTRADAS_INTERFAZ["elegir_opcion"]
        self._iterador_campos_actual = iter(self._definicion_campos_actual)
        self._parametros_recolectados = {}
        self._estado_interfaz = {
            "grupo_acciones": self._interfaz.obtener_grupo_acciones_actual(),
            "respuesta": None,
            "error": None,
            "campo_actual": None,
            "mensaje_campo": None,
            "modo": "menu"  # o "accion"
        }


    def bucle_general(self):
        while self._corriendo:
            self._renderizador.borrar_pantalla()

            # Actualiza siempre el grupo de acciones por si cambia dinámicamente
            self._estado_interfaz["grupo_acciones"] = self._interfaz.obtener_grupo_acciones_actual()

            campo_info = self._interfaz.siguiente_campo_de_entrada(
                self._definicion_campos_actual,
                self._tipo_accion_actual,
                self._iterador_campos_actual,
            )

            if campo_info["datos"]["completado"]:
                tipo_accion = self._tipo_accion_actual
                parametros = self._parametros_recolectados.copy()

                # Reset estado de entrada
                self._reiniciar_estado_entrada()

                if tipo_accion == "elegir_opcion":
                    seleccion = self._interfaz.elegir_opcion(
                        self._estado_interfaz["grupo_acciones"],
                        parametros.get("opcion_elegida")
                    )
                    if not seleccion["exito"]:
                        self._estado_interfaz["error"] = seleccion["error"]
                        continue

                    self._tipo_accion_actual = seleccion["datos"]["tipo_accion"]
                    self._definicion_campos_actual = ENTRADAS_INTERFAZ.get(self._tipo_accion_actual, [])
                    self._iterador_campos_actual = iter(self._definicion_campos_actual)
                    continue

                respuesta = self.procesar_accion(tipo_accion, parametros)

                ##################################################################
                # Testing
                print(f"tipo_accion: {tipo_accion}, parametros: {parametros} ")
                print(f"respuesta: {respuesta}")
                stop = input("----------------------------------")
                self._renderizador.borrar_pantalla()
                ##################################################################
                
                if tipo_accion in ACCIONES_MENU_TERMINAL:
                    self._estado_interfaz["modo"] = "menu"
                elif tipo_accion in ACCIONES:
                    self._estado_interfaz["modo"] = "accion"
                
                self._estado_interfaz["respuesta"] = respuesta

                ##################################################################
                # Testing
                coso = self._estado_interfaz
                print(coso)
                input("---------------------------------")
                self._renderizador.borrar_pantalla()
                ##################################################################

                self._renderizador.renderizar_pantalla(self._estado_interfaz)

                # Solicitar confirmación
                if tipo_accion in ACCIONES and self._estado_interfaz["modo"] == "accion":
                    self._renderizador.solicitar_confirmacion()
                
                # Resetear respuesta
                self._estado_interfaz["respuesta"] = None
                

                if tipo_accion == "terminar_programa":
                    self._corriendo = False

            else:
                campo = campo_info["datos"]["campo_actual"]
                self._estado_interfaz["campo_actual"] = campo
                self._estado_interfaz["mensaje_campo"] = campo_info["datos"]["mensaje"]

                if self._tipo_accion_actual == "elegir_opcion":
                    self._estado_interfaz["modo"] = "menu"
                else:
                    self._estado_interfaz["modo"] = "accion"

                # Generar respuesta parcial para mostrar campos rellenados hasta ahora
                if self._tipo_accion_actual in LINEAS_RESPUESTA:
                    self._estado_interfaz["respuesta"] = self.generar_respuesta_parcial(
                        self._tipo_accion_actual,
                        self._parametros_recolectados
                    )
                else:
                    self._estado_interfaz["respuesta"] = None

                self._renderizador.renderizar_pantalla(self._estado_interfaz)
                
                # Luego, pedir nueva entrada
                entrada = self._renderizador.solicitar_entrada()

                if not entrada:
                    self._estado_interfaz["error"] = f"{campo}_vacio"
                else:
                    self._parametros_recolectados[campo] = entrada
                    self._estado_interfaz["error"] = None


    def procesar_accion(self, tipo_accion: str, parametros: dict) -> dict:
        """
        Procesa la acción seleccionada desde la interfaz terminal.
        """

        if tipo_accion in ACCIONES:
            respuesta = self._controlador_cajero.procesar_peticion(tipo_accion, parametros)

            # Si la acción genera un submenú y fue exitosa, abrir ese menú
            if tipo_accion in ACCION_GENERADOR_SUBMENU and respuesta.get("exito"):
                nombre_menu_destino = ACCION_GENERADOR_SUBMENU[tipo_accion]
                self._ejecutar_abrir_menu(nombre_menu_destino)

            return respuesta

        elif tipo_accion in ACCIONES_MENU_TERMINAL:
            accion = ACCIONES_MENU_TERMINAL[tipo_accion]
            funcion = accion.get("funcion")
            if callable(funcion):
                # Las acciones especiales del menú devuelven respuesta semántica
                return funcion(self._interfaz)
                

        return RespuestaSemantica(tipo_respuesta="accion_desconocida") \
            .con_error("accion_invalida") \
            .obtener_diccionario()

    def _ejecutar_abrir_menu(self, nombre_menu_destino: str):
        """
        Ejecuta la acción 'menu_abrir' con el nombre del menú destino.
        """
        abrir_menu = ACCIONES_MENU_TERMINAL.get("menu_abrir")
        if abrir_menu and "funcion" in abrir_menu:
            funcion = abrir_menu["funcion"]
            if callable(funcion):
                funcion(self._interfaz, nombre_menu_destino)


    def _reiniciar_estado_entrada(self):
        self._parametros_recolectados.clear()
        self._tipo_accion_actual = "elegir_opcion"
        self._definicion_campos_actual = ENTRADAS_INTERFAZ["elegir_opcion"]
        self._iterador_campos_actual = iter(self._definicion_campos_actual)

    def generar_respuesta_parcial(self, tipo_accion: str, parametros: dict) -> dict:
        return {
            "tipo_accion": tipo_accion,
            "datos": parametros,
            "exito": True  # se considera siempre "exitosa" porque es solo para mostrar
        }
