class Linea:
    @staticmethod
    def texto(contenido: str, alineacion: str = "izquierda", id: str = None) -> dict:
        linea = {
            "contenido": contenido,
            "tipo": "texto"
        }
        if alineacion:
            linea["alineacion"] = alineacion
        if id:
            linea["id"] = id
        return linea

    @staticmethod
    def input(contenido: str, id: str = None) -> dict:
        linea = {
            "contenido": contenido,
            "tipo": "input"
        }
        if id:
            linea["id"] = id
        return linea

    @staticmethod
    def linea_vacia(cantidad: int = 1) -> list[dict]:
        if cantidad <= 0:
            cantidad = 1
        return [{"contenido": "", "tipo": "lineaVacia"} for _ in range(cantidad)]

    @staticmethod
    def alinear(linea: dict, alineacion: str) -> dict:
        linea["alineacion"] = alineacion
        return linea
