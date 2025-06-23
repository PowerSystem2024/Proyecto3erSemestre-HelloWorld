ACCIONES = {
    # Acciones de Usuario
    "consultar_saldo": {
        "nombre": "Consultar Saldo",
        "funcion": lambda c, p: c.obtener_usuario_actual().consultar_saldo()
    },
    "retirar_dinero": {
        "nombre": "Retirar Dinero",
        "funcion": lambda c, p: c.obtener_usuario_actual().retirar_dinero(p.get("cantidad_dinero"))
    },
    "depositar_dinero": {
        "nombre": "Depositar Dinero",
        "funcion": lambda c, p: c.obtener_usuario_actual().depositar_dinero(p.get("cantidad_dinero"))
    },
    "transferir_dinero": {
        "nombre": "Transferir Dinero",
        "funcion": lambda c, p: c.obtener_usuario_actual().transferir_dinero(
            p.get("cantidad_dinero"),
            p.get("usuario_destino")
        )
    },

    # Acciones de Cajero
    "terminar_programa": {
        "nombre": "Terminar Programa",
        "funcion": lambda c, p: c.terminar_programa()
    },
    "mostrar_usuarios_registrados": {
        "nombre": "Listar Usuarios",
        "funcion": lambda c, p: c.mostrar_usuarios_registrados()
    },
    "generar_usuario": {
        "nombre": "Crear Usuario",
        "funcion": lambda c, p: c.generar_usuario(
            p.get("nombre_usuario"),
            p.get("contraseña"),
            p.get("saldo_inicial")
        )
    },
    "iniciar_sesion": {
        "nombre": "Iniciar Sesión",
        "funcion": lambda c, p: c.iniciar_sesion(
            p.get("nombre_usuario"),
            p.get("contraseña")
        )
    },

}


"""
    # Acciones de Menú
    "salir": {
        "nombre": "Salir",
        "funcion": lambda c, p: RespuestaSemantica(tipo_respuesta="salir").con_exito().obtener_diccionario()
    },"""