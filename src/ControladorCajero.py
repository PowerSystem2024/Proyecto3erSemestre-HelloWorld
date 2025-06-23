from .RespuestaSemantica import RespuestaSemantica
from .Cajero import Cajero
from .Acciones import ACCIONES
from .ManejadorEntrada import ManejadorEntrada

class ControladorCajero:
    def __init__(self, manejador_entrada: ManejadorEntrada):
        self._cajero = Cajero()
        self._cajero.inicializar_sistema()
        self.manejador_entrada = manejador_entrada

    def procesar_peticion(self, tipo_accion: str) -> dict:
        parametros = self.manejador_entrada.solicitar_datos(tipo_accion)
        if tipo_accion in ACCIONES:
            return ACCIONES[tipo_accion]["funcion"](self._cajero, parametros)
        else:
            return RespuestaSemantica(tipo_respuesta="accion_desconocida") \
                .con_error("accion_invalida") \
                .obtener_diccionario()