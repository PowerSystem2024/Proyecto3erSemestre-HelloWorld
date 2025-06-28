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

