import os
import time
from .ConfiguracionGrafica import *
from ..Acciones import *
from .Linea import Linea

LINEAS_RESPUESTA = {
    "iniciar_sesion": [
        Linea.texto("Nombre de Usuario: {usuario}", indentacion_horizontal=1, alineacion_vertical="arriba"),
        Linea.texto("Contraseña: ******", indentacion_horizontal=1, alineacion_vertical="arriba", indentacion_vertical=1),
        Linea.texto("Inicio de Sesión Exitoso", alineacion_horizontal="centro", alineacion_vertical="centro", tipo="exito"),
        Linea.texto("Bienvenido {usuario}", alineacion_horizontal="centro", alineacion_vertical="centro", indentacion_vertical=1, tipo="exito")
    ],
    "consultar_saldo": [
        Linea.texto("Cuenta: {cuenta}", indentacion_horizontal=1, alineacion_vertical="arriba"),
        Linea.texto("Saldo actual: ${saldo}", indentacion_horizontal=1, alineacion_vertical="arriba", indentacion_vertical=1),
        Linea.texto("Consulta completada", alineacion_horizontal="centro", alineacion_vertical="abajo", tipo="info")
    ],
}



class RenderizadorInterfazTerminal:
    def __init__(self):
        pass

    def borrar_pantalla(self):
        """
        Limpia la consola dependiendo del sistema operativo.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def renderizar_pantalla(self, estado: dict):
        lineas = []

        if estado["modo"] == "menu":
            lineas.extend(self._generar_lineas_menu(estado["grupo_acciones"]))

        elif estado["modo"] == "accion":
            lineas.extend(self._generar_lineas_respuesta(estado.get("respuesta")))

        # Entrada
        if estado.get("mensaje_campo"):
            linea_entrada = self._renderizar_entrada(estado["mensaje_campo"])
            lineas.append(linea_entrada)

        # Imprimir todo junto
        self.escribir_con_retraso(lineas)



    def _generar_lineas_menu(self, grupo_acciones: list[str]) -> list[str]:
        celdas_con_opciones = []
        celdas_con_numeros = []
        celdas_con_flechas = []
        filas_menu = []
        i = 0
        numero_opciones = len(grupo_acciones)

        for accion in grupo_acciones:
            celdas_con_opciones.append(self._insertar_contenido_en_celda(accion, CELDA_RECTANGULAR))

        for idx in range(numero_opciones):
            celdas_con_numeros.append(self._insertar_contenido_en_celda(idx + 1, CELDA_NUMERICA))
            flecha = CELDA_FLECHA_IZQUIERDA if idx % 2 == 0 else CELDA_FLECHA_DERECHA
            celdas_con_flechas.append(flecha)

        # Rellenar si hay menos de las opciones visibles máximas
        for _ in range(numero_opciones, MAX_OPCIONES_VISIBLES):
            celdas_con_opciones.append(CELDA_RECTANGULAR_VACIA)
            celdas_con_numeros.append(CELDA_NUMERICA_VACIA)
            celdas_con_flechas.append(CELDA_FLECHA_VACIA)

        for fila in range(NUMERO_FILAS_MENU):
            for subfila in range(ALTURA_GENERAL_CELDA):
                filas_menu.append(
                    f"{celdas_con_numeros[i][subfila]}"
                    f"{celdas_con_flechas[i][subfila]}"
                    f"{celdas_con_opciones[i][subfila]}"
                    f"{Graficos.ESPACIO * ESPACIO_ENTRE_COLUMNAS_MENU}"
                    f"{celdas_con_opciones[i + 1][subfila]}"
                    f"{celdas_con_flechas[i + 1][subfila]}"
                    f"{celdas_con_numeros[i + 1][subfila]}"
                )
            filas_menu.extend([""] * ESPACIO_ENTRE_FILAS_MENU)
            i += 2

        return filas_menu

    def _insertar_contenido_en_celda(self, contenido, celda: list[str]) -> list[str]:
        """
        Inserta un texto (derivado de un nombre de acción o número) centrado 
        vertical y horizontalmente dentro de una celda.

        Parámetros:
            - contenido: clave de acción (str) o número entero.
            - celda: lista de strings que representan una celda.

        Retorna:
            - Nueva lista de strings con el contenido insertado en la línea central.
        """
        if isinstance(contenido, str):
            if contenido in ACCIONES:
                texto = ACCIONES[contenido]["nombre"]
            elif contenido in ACCIONES_MENU_TERMINAL:
                texto = ACCIONES_MENU_TERMINAL[contenido]["nombre"]
            else:
                raise ValueError(f"Clave de acción desconocida: '{contenido}'")
        elif isinstance(contenido, int):
            texto = str(contenido)
        else:
            raise TypeError("El contenido debe ser una cadena válida o un número entero.")

        alto = len(celda)
        ancho = len(celda[0])
        indice_central = alto // 2
        espacio_interno = ancho - 2

        if espacio_interno < len(texto) + 2:
            raise ValueError("La celda es demasiado angosta para insertar el texto.")

        texto_centrado = texto.center(espacio_interno)
        borde_izquierdo = celda[indice_central][0]
        borde_derecho = celda[indice_central][-1]
        nueva_linea = f"{borde_izquierdo}{texto_centrado}{borde_derecho}"

        celda_modificada = celda.copy()
        celda_modificada[indice_central] = nueva_linea

        return celda_modificada


    def _renderizar_entrada(self, mensaje: str) -> str:
        """
        Devuelve una línea con el mensaje para solicitar entrada del usuario,
        sin imprimirla. Deberá ser añadida al final de la pantalla renderizada.

        Parámetro:
            - mensaje: Texto a mostrar antes del input.

        Retorna:
            - Línea de texto formateada.
        """
        return mensaje + " "


    def _renderizar_error(self, codigo_error):
        print(f"\n[ERROR] {codigo_error}")

    def _renderizar_respuesta(self, respuesta):
        print("\n[RESPUESTA]")
        for clave, valor in respuesta["datos"].items():
            print(f"{clave}: {valor}")

    def solicitar_entrada(self):
        return input().strip()
    
    def escribir_con_retraso(self, lineas: list[str], delay=0.05):
        for i, linea in enumerate(lineas):
            if i == len(lineas) - 1:
                print(linea, end="")
            else:
                print(linea)
            time.sleep(delay)


    def _generar_lineas_respuesta(self, respuesta):
        celda = CELDA_ACCCION.copy()
        datos = respuesta.get("datos", {})
        tipo_accion = respuesta.get("tipo_accion")
        lineas = self.obtener_lineas_formateadas(tipo_accion, datos)
        return self._insertar_lineas_en_celda_accion(celda, lineas)

    @staticmethod
    def obtener_lineas_formateadas(tipo_accion: str, datos: dict) -> list[dict]:
        plantilla = LINEAS_RESPUESTA.get(tipo_accion, [])
        lineas = []
        for linea in plantilla:
            contenido = linea["contenido"].format_map(DefaultDictConVacios(datos))
            linea_formateada = {
                **linea,
                "contenido": contenido
            }
            lineas.append(linea_formateada)
        return lineas


    

    def _insertar_lineas_en_celda_accion(self, celda: list[str], lineas_formateadas: list[dict]) -> list[str]:
        """
        Inserta múltiples líneas formateadas en la celda de acción según su indentación y alineación.

        Parámetros:
            celda (list[str]): lista de cadenas que representan la celda (cada string es una fila).
            lineas_formateadas (list[dict]): lista de líneas con formato (dict) generadas por Linea.texto.

        Retorna:
            list[str]: celda modificada con las líneas insertadas.
        """
        celda_modificada = celda.copy()
        alto = len(celda)
        if alto == 0:
            return celda_modificada

        ancho = len(celda[0])
        if ancho < 2:
            return celda_modificada

        espacio_interno = ancho - 2  # excluye bordes

        for linea in lineas_formateadas:

            identacion_vertical = linea.get("indentacion_vertical", 0)
            alineacion_vertical = linea.get("alineacion_vertical", "arriba")
            

            if alineacion_vertical == "centro":
                fila = alto // 2 + identacion_vertical
            elif alineacion_vertical == "abajo":
                fila = alto - 1 - identacion_vertical
            else:  # "arriba" u otra cosa
                fila = 1 + identacion_vertical

            fila = max(1, min(fila, alto - 2))

            if fila < 0 or fila >= alto:
                continue

            contenido = linea.get("contenido", "")
            indentacion_horizontal = linea.get("indentacion_horizontal", 0)
            alineacion_horizontal = linea.get("alineacion_horizontal", "izquierda")
            

            # Se añade indentación horizontal en espacios
            contenido = " " * indentacion_horizontal + contenido
            if len(contenido) > espacio_interno:
                contenido = contenido[:espacio_interno]  # truncar si es muy largo

            # Ajuste según alineación horizontal
            if alineacion_horizontal == "izquierda":
                contenido_ajustado = contenido.ljust(espacio_interno)
            elif alineacion_horizontal == "centro":
                contenido_ajustado = contenido.center(espacio_interno)
            elif alineacion_horizontal == "derecha":
                contenido_ajustado = contenido.rjust(espacio_interno)
            else:
                contenido_ajustado = contenido.ljust(espacio_interno)  # por defecto

            # Reconstruir la línea con bordes
            linea_celda = celda_modificada[fila]
            borde_izquierdo = linea_celda[0]
            borde_derecho = linea_celda[-1]

            nueva_linea = f"{borde_izquierdo}{contenido_ajustado}{borde_derecho}"

            celda_modificada[fila] = nueva_linea

        return celda_modificada
    
    
    def solicitar_confirmacion(self):
        print("\nPresionar tecla ENTER para continuar...")
        input()

class DefaultDictConVacios(dict):
    def __missing__(self, key):
        return ""

