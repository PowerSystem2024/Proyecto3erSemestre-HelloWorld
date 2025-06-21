from src import * 

# datos:
# usuario: admin
# contraseña: 1234
# saldo incial: 100000 


if __name__ == "__main__":
    atm = Cajero()
    atm.inicializar_sistema()

    acciones_submenu_escribir = [
        [
            AccionBasica("Escribir texto"),
            AccionBasica("Editar texto"),
            AccionBasica("Borrar texto"),
            AccionBasica("Guardar texto"),
            AccionBasica("Renombrar archivo"),
            AccionBasica("Ver historial"),
            Volver("Volver"),
            Siguiente("Siguiente")
        ],
        [
            AccionBasica("Seleccionar fuente"),
            AccionBasica("Cambiar tamaño"),
            AccionBasica("Aplicar negrita"),
            AccionBasica("Aplicar cursiva"),
            AccionBasica("Cambiar color"),
            AccionBasica("Centrar texto"),
            Anterior("Anterior"),
            Siguiente("Siguiente")
        ],
        [
            AccionBasica("Buscar palabra"),
            AccionBasica("Reemplazar palabra"),
            AccionBasica("Contar palabras"),
            AccionBasica("Ver estadísticas"),
            AccionBasica("Corregir ortografía"),
            AccionBasica("Exportar archivo"),
            Anterior("Anterior"),
            Siguiente("Siguiente")
        ],
        [
            Anterior("Anterior")
        ]
    ]

    acciones_menu_secreto = [
        [
            ConsultarSaldo("Consultar Saldo", atm),  # ToDo: Esto en realidad me podría generar un submenu que tiene Consultar Saldo Dolares u Pesos
            RetirarSaldo("Retirar Saldo", atm),
            TransferirSaldo("Transferir Saldo", atm),
            DepositarSaldo("Depositar Saldo", atm),
            ListarUsuarios("Listar Usuarios", atm),
            CrearUsuario("Crear Usuario", atm),
            Salir("Salir"),
            Siguiente("Siguiente")
        ],
        [
            TerminarPrograma("Terminar Programa", atm),
            AccionBasica("Restar B"),
            AccionBasica("Multiplicar B"),
            AccionBasica("Dividir B"),
            AccionBasica("Potencia B"),
            AccionBasica("Raíz B"),
            Anterior("Anterior"),
            Siguiente("Siguiente")
        ],
        [
            CrearSubMenu("Escribir", acciones_submenu_escribir),
            AccionBasica("Restar C"),
            AccionBasica("Multiplicar C"),
            AccionBasica("Dividir C"),
            AccionBasica("Potencia C"),
            AccionBasica("Raíz C"),
            Anterior("Anterior"),
            Siguiente("Siguiente")
        ],
    ]


    acciones_menu_principal = [
        [
            ConsultarSaldo("Consultar Saldo", atm),  # ToDo: Esto en realidad me podría generar un submenu que tiene Consultar Saldo Dolares u Pesos
            RetirarSaldo("Retirar Saldo", atm),
            TransferirSaldo("Transferir Saldo", atm),
            DepositarSaldo("Depositar Saldo", atm),
            Salir("Salir"),
        ],
    ]

    acciones_menu_entrada = [
        [
            IniciarSesion("Iniciar Sesión", acciones_menu_principal, atm, acciones_menu_secreto),
            Registrarse("Registrarse", atm),
        ],
    ]

    menu_cajero = Menu(acciones_menu_entrada)
    menu_cajero.crear_menu()
