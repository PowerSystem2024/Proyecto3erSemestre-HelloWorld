import time
import os

def escribir_con_retraso(texto, delay=0.05):
    """
    Escribe un texto línea por línea con un retraso opcional.

    Parámetros:
        texto (str): Texto que se desea mostrar.
        delay (float): Tiempo de espera entre líneas.
    """
    for linea in texto.splitlines():
        print(linea)
        time.sleep(delay)

def esperar_tiempo(delay = 5):
     time.sleep(delay)

def borrar_pantalla():
        """
        Limpia la consola dependiendo del sistema operativo.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_con_delay(mensaje, delay=0.8):
    print(mensaje)
    time.sleep(delay)