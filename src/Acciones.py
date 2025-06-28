ACCIONES = {
    # Acciones de Usuario
    "consultar_saldo": {
        "nombre": "Consultar Saldo",
        "funcion": lambda c, p: c.obtener_usuario_actual().consultar_saldo(),
        "parametros": []
    },
    "retirar_dinero": {
        "nombre": "Retirar Dinero",
        "funcion": lambda c, p: c.obtener_usuario_actual().retirar_dinero(p.get("cantidad_dinero")),
        "parametros": ["cantidad_dinero"]
    },
    "depositar_dinero": {
        "nombre": "Depositar Dinero",
        "funcion": lambda c, p: c.obtener_usuario_actual().depositar_dinero(p.get("cantidad_dinero")),
        "parametros": ["cantidad_dinero"]
    },
    "transferir_dinero": {
        "nombre": "Transferir Dinero",
        "funcion": lambda c, p: c.obtener_usuario_actual().transferir_dinero(
            p.get("cantidad_dinero"),
            p.get("usuario_destino")
        ),
        "parametros": ["cantidad_dinero", "usuario_destino"]
    },

    # Acciones de Cajero
    "terminar_programa": {
        "nombre": "Terminar Programa",
        "funcion": lambda c, p: c.terminar_programa(),
        "parametros": []
    },
    "mostrar_usuarios_registrados": {
        "nombre": "Listar Usuarios",
        "funcion": lambda c, p: c.mostrar_usuarios_registrados(),
        "parametros": []
    },
    "generar_usuario": {
        "nombre": "Crear Usuario",
        "funcion": lambda c, p: c.generar_usuario(
            p.get("nombre_usuario"),
            p.get("contraseña"),
            p.get("saldo_inicial")
        ),
        "parametros": ["nombre_usuario", "contraseña", "saldo_inicial"]
    },
    "iniciar_sesion": {
        "nombre": "Iniciar Sesión",
        "funcion": lambda c, p: c.iniciar_sesion(
            p.get("nombre_usuario"),
            p.get("contraseña")
        ),
        "parametros": ["nombre_usuario", "contraseña"]
    },
    "cerrar_sesion": {
        "nombre": "Cerrar Sesión",
        "funcion": lambda c, p: c.cerrar_sesion(),
        "parametros": []
    },
    "registrar_usuario": {
        "nombre": "Registrar Usuario",
        "funcion": lambda c, p: c.registrar_usuario(
            p.get("nombre_usuario"),
            p.get("contraseña")
        ),
        "parametros": ["nombre_usuario", "contraseña"]
    },

}

ACCIONES_MENU_TERMINAL = {
    "menu_abrir": {
        "nombre": "Abrir menú",
        "funcion": lambda interfaz, nombre_menu: interfaz.menu_abrir(nombre_menu),
        "parametros": ["nombre_menu"]
    },
    "menu_volver": {
        "nombre": "Volver",
        "funcion": lambda interfaz: interfaz.menu_volver(),
        "parametros": []
    },
    "menu_siguiente": {
        "nombre": "Siguiente",
        "funcion": lambda interfaz: interfaz.menu_siguiente(),
        "parametros": []
    },
    "menu_anterior": {
        "nombre": "Anterior",
        "funcion": lambda interfaz: interfaz.menu_anterior(),
        "parametros": []
    },
}