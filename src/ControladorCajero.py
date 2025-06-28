from .RespuestaSemantica import RespuestaSemantica
from .Cajero import Cajero
from .Acciones import ACCIONES


class ControladorCajero:
    def __init__(self):
        self._cajero = Cajero()
        self._cajero.inicializar_sistema()
        #self.db = self._cajero.obtener_base_de_datos()


    def procesar_peticion(self, tipo_accion: str, parametros: dict) -> dict:

        accion = ACCIONES.get(tipo_accion)
        
        if accion and "funcion" in accion and callable(accion["funcion"]):
            return accion["funcion"](self._cajero, parametros)

        return RespuestaSemantica(tipo_respuesta="accion_desconocida") \
            .con_error("accion_invalida") \
            .obtener_diccionario()
