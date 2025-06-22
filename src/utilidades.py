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


def borrar_pantalla():
        """
        Limpia la consola dependiendo del sistema operativo.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

def validar_valor_positivo(valor):
    try:
        v = float(valor)
    except (ValueError, TypeError):
        return False, "entrada_invalida"
    if v <= 0:
        return False, "cantidad_no_positiva"
    return True, v

def validar_valor_no_negativo(valor):
    try:
        v = float(valor)
    except (ValueError, TypeError):
        return False, "entrada_invalida"
    if v < 0:
        return False, "cantidad_negativa"
    return True, v

def validar_datos_usuario(nombre: str, contraseña: str, saldo) -> tuple[bool, tuple | str]:
    if not isinstance(nombre, str) or not nombre.strip():
        return False, "nombre_usuario_invalido"
    if not isinstance(contraseña, str) or not contraseña.strip():
        return False, "contraseña_invalida"
    
    valido, resultado = validar_valor_no_negativo(saldo)
    if not valido:
        return False, resultado
    saldo = resultado  # resultado es el saldo convertido a float

    return True, (nombre.strip(), contraseña.strip(), saldo)



def validar_usuario(usuario):
    """
    Verifica que el objeto tenga la estructura y contenido mínimos de un usuario válido.

    Retorna:
        - (True, None): si el usuario es válido.
        - (False, codigo_error): si no lo es.
    """
    if usuario is None:
        return False, "usuario_invalido"

    if not hasattr(usuario, "id_usuario") or not isinstance(usuario.id_usuario, int):
        return False, "id_usuario_invalido"

    if not hasattr(usuario, "nombre") or not isinstance(usuario.nombre, str):
        return False, "nombre_usuario_invalido"

    if not hasattr(usuario, "saldo") or not isinstance(usuario.saldo, (int, float)):
        return False, "saldo_no_valido"

    return True, None

CODIGOS_ERROR = {
    # Errores de entrada
    "entrada_invalida": "La entrada proporcionada no es válida o no se pudo convertir a número.",
    "cantidad_no_positiva": "La cantidad debe ser mayor a cero.",
    "cantidad_negativa": "La cantidad no debe ser negativa.",

    # Errores relacionados con saldo
    "saldo_no_valido": "El saldo actual no es un valor numérico.",
    "saldo_insuficiente": "No hay suficiente saldo para realizar la operación.",


    # Errores relacionados con usuario
    "usuario_invalido": "El objeto no representa un usuario válido.",
    "id_usuario_invalido": "El ID del usuario debe ser un número entero.",
    "transferencia_a_mismo_usuario": "No se puede transferir dinero al mismo usuario.",
    "sin_usuarios_registrados": "No hay usuarios registrados en el sistema.",
    "nombre_usuario_invalido": "El nombre de usuario no es válido.",
    "contraseña_invalida": "La contraseña no es válida.",
    "usuario_ya_existe": "El nombre de usuario ya está registrado.",

    # Errores relacionados con sesion
    "credenciales_invalidas": "El nombre de usuario o la contraseña son incorrectos.",
    "demasiados_intentos": "Se han agotado los intentos de inicio de sesión. Por favor, intente más tarde.",


}

NOMBRES_ACCIONES = {
    "consultar_saldo": "Consultar Saldo",
    "retirar_dinero": "Retirar Dinero",
    "depositar_dinero": "Depositar Dinero",
    "transferir_dinero": "Transferir Dinero",
    "terminar_programa": "Terminar Programa"
}
