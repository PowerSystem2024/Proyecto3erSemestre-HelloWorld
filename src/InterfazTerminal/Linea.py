class Linea:
    @staticmethod
    def texto(
        contenido: str,
        id: str = None,
        tipo: str = "texto",
        alineacion_horizontal: str = "izquierda",
        alineacion_vertical: str = "centro",
        indentacion_horizontal: int = 0,
        indentacion_vertical: int = 0
    ) -> dict:
        if alineacion_horizontal not in {"izquierda", "centro", "derecha"}:
            alineacion_horizontal = "izquierda"
        if alineacion_vertical not in {"arriba", "centro", "abajo"}:
            alineacion_vertical = "centro"
        linea = {
            "contenido": contenido,
            "tipo": tipo,
            "alineacion_horizontal": alineacion_horizontal,
            "alineacion_vertical": alineacion_vertical,
            "indentacion_horizontal": indentacion_horizontal,
            "indentacion_vertical": indentacion_vertical
        }
        if id:
            linea["id"] = id
        return linea

    @staticmethod
    def alinear_horizontal(linea: dict, alineacion: str) -> dict:
        linea["alineacion_horizontal"] = alineacion
        return linea

    @staticmethod
    def alinear_vertical(linea: dict, alineacion: str) -> dict:
        linea["alineacion_vertical"] = alineacion
        return linea

    @staticmethod
    def linea_vacia(
        cantidad: int = 1,
        alineacion_vertical: str = "centro",
        indentacion_vertical: int = 0
    ) -> list[dict]:
        if cantidad <= 0:
            cantidad = 1
        return [
            Linea.texto(
                contenido="",
                tipo="lineaVacia",
                alineacion_horizontal="izquierda",
                alineacion_vertical=alineacion_vertical,
                indentacion_horizontal=0,
                indentacion_vertical=indentacion_vertical
            )
            for _ in range(cantidad)
        ]
