
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

    # Errores relacionados a tipo Accion
    "accion_invalida": "La acción solicitada no es válida o no está disponible en el sistema.",

    # Errores relacionados a Menu Terminal
    "estructura_invalida_menu": "El parámetro 'acciones' debe ser una lista de listas.",
    "menu_no_definido": "El menú '{nombre_menu}' no está definido correctamente.",
    "maximo_opciones_excedido": "Cada grupo debe tener como máximo '{MAX_OPCIONES_VISIBLES}' acciones.",
    "grupo_acciones_vacio": "Cada grupo de acciones debe tener al menos una acción.",
    "tipo_accion_no_es_cadena": "Cada acción debe ser una cadena de texto.",
    "accion_no_definida": "La acción '{tipo_accion}' no está definida en el sistema.",
    "accion_sin_nombre": "La acción '{tipo_accion}' no tiene un nombre definido.",
    "accion_sin_funcion": "La acción '{tipo_accion}' no tiene una función válida.",
    "accion_menu_no_definida": "La acción de menú '{tipo_accion}' no está definida.",
    "accion_menu_sin_nombre": "La acción de menú '{tipo_accion}' no tiene nombre.",
    "accion_menu_sin_funcion": "La acción de menú '{tipo_accion}' no tiene función.",
    "configuracion_menu_invalida": "La configuración del menú '{nombre_menu}' no es una lista de listas válida."
}

class ErrorInterfazTerminal(Exception):
        def __init__(self, codigo_error: str, **kwargs):
            self.codigo = codigo_error
            mensaje = CODIGOS_ERROR.get(codigo_error, "Error desconocido.")
            try:
                self.mensaje = mensaje.format(**kwargs)
            except KeyError:
                self.mensaje = mensaje
            super().__init__(self.mensaje)