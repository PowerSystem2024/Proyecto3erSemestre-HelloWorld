MENU_TERMINAL = {
    "menu_entrada": [
        ["iniciar_sesion", "registrar_usuario"],
    ],
    "menu_principal": [
        ["consultar_saldo", "retirar_dinero", "depositar_dinero", "transferir_dinero", "cerrar_sesion"],
    ],
    # Otros menús...
}

ACCION_GENERADOR_SUBMENU = {
    "iniciar_sesion": "menu_principal",
    "cerrar_sesion": "menu_entrada",
}

ENTRADAS_INTERFAZ = {
    "iniciar_sesion": {
        "nombre_usuario": {
            "mensaje": "Ingresar nombre de usuario: "
        },
        "contraseña": {
            "mensaje": "Ingresar contraseña: "
        }
    },
    "generar_usuario": {
        "usuario": {
            "mensaje": "Nombre de usuario nuevo: "
        },
        "contraseña": {
            "mensaje": "Contraseña inicial: "
        },
        "saldo": {
            "mensaje": "Saldo inicial: ",
        }
    },
    "elegir_opcion": {
        "opcion_elegida": {
            "mensaje" : "Elegir opción: "
        }
    }
}