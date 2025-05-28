def iniciar_sesion():
    # TODO: crear la función para la creación de la base de datos
    db = BaseDeDatos()                # Crear instancia de la base de datos
    db.conectar()                     # Conectar a la base de datos
    db.crear_tabla_usuarios()         # Crear la tabla de usuarios si no existe

    # Si no hay usuarios en la base de datos, se crea un usuario por defecto
    if db.verificar_usuarios_existentes() == 0:
        db.crear_usuario_inicial()

    intentos = 3  # Se permiten hasta 3 intentos de inicio de sesión

    while intentos > 0:
        # Pedir al usuario sus credenciales
        usuario = input('Ingrese su nombre de usuario: ')
        contraseña = input('Ingrese su contraseña: ')

        # Verificar si las credenciales son correctas
        resultado = db.autenticar_usuario(usuario, contraseña)

        if resultado:
            id_usuario, saldo = resultado  # Si es válido, se obtiene el ID y saldo del usuario
            (f'Bienvenido {usuario}')
            
            # Crear un objeto Usuario con la información autenticada
            usuario_actual = (id_usuario, usuario, saldo, db)

            # Devolvemos el usuario autenticado para usarlo en el resto del sistema
            return usuario_actual
        else:
            intentos -= 1  # Reducir el contador de intentos
            (f'Usuario o contraseña incorrectos. Intentos restantes: {intentos}')
            
            if intentos == 0:
                ('Demasiados intentos. Reinicie el programa e intente de nuevo.')
                break

    db.cerrar_conexion()  # Cerrar conexión en cualquier caso
    return None  # Si no se autenticó correctamente
