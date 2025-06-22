class RespuestaSemantica:
    def __init__(self, tipo_respuesta: str):
        self.tipo_respuesta = tipo_respuesta
        self.exito = None
        self.datos = {}
        self.error = None

    def con_exito(self, datos: dict = None):
        self.exito = True
        self.datos = datos or {}
        return self

    def con_error(self, codigo_error: str):
        self.exito = False
        self.error = codigo_error
        return self

    def obtener_diccionario(self) -> dict:
        return {
            "tipo_respuesta": self.tipo_respuesta,
            "exito": self.exito,
            "datos": self.datos,
            "error": self.error
        }
