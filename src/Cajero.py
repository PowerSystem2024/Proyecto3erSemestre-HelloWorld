from .BaseDeDatos import BaseDeDatos
from .utilidades import *
from .Usuario import Usuario
import sys

"""A continuación, seleccione la operación que desea realizar
                1 - Consultar saldo
                2 - Retirar saldo
                3 - Transferir
                4 - Depositar saldo
                5 - Crear nuevos usuarios
                6 - Mostrar usuarios registrados
                7 - Salir
"""

class Cajero:
    def __init__(self):
        self.db = BaseDeDatos()                # Crear instancia de la base de datos
        self._usuario_actual = None
    
    def terminar_programa(self):
        imprimir_con_delay('Saliendo del Sistema...')
        self.db.cerrar_conexion()
        sys.exit()
    
    # Implementado como Accion ListarUsuarios # Solo accesible para admin
    def mostrar_usuarios_registrados(self): 
        """Muestra la lista de usuarios registrados en el sistema"""
        usuarios = self.db.obtener_usuarios()
        if not usuarios:
            imprimir_con_delay("No hay usuarios registrados en el sistema.") # ToDo se debería retornar una lista de cadenas para poder ser imprimidos en el menu acordemente
            return
            
        imprimir_con_delay("\n--- USUARIOS REGISTRADOS ---")
        for i, nombre in enumerate(usuarios, 1):
            imprimir_con_delay(f"{i}. {nombre}")
        imprimir_con_delay("-------------------------\n")
    
    # Implementado como Accion CrearUsuario # Solo admin
    def generar_usuario(self): # Esto debe de ser un metodo admin
        try:
            nuevo_nombre_usuario = input('Ingrese el nombre del nuevo usuario: ')

            # Verificar si el usuario ya existe en la base de datos
            if self.db.usuario_existe(nuevo_nombre_usuario):
                imprimir_con_delay(f'El usuario "{nuevo_nombre_usuario}" ya existe. No se puede crear.')
                return  # Evita continuar si el usuario ya existe

            nueva_contraseña_usuario = input('Ingrese la contraseña del nuevo usuario: ')
            entrada = input('Ingrese el saldo inicial del nuevo usuario: ')
            nuevo_saldo_usuario = float(entrada)
            if nuevo_saldo_usuario < 0:
                imprimir_con_delay("El saldo no puede ser negativo.")
                return

            # Crear el usuario en la base de datos
            self.db.crear_nuevo_usuario(nuevo_nombre_usuario, nueva_contraseña_usuario, nuevo_saldo_usuario)

            # No necesitamos crear un objeto Usuario aquí, solo estamos registrando usuarios
            # El objeto Usuario se crea cuando alguien inicia sesión
            imprimir_con_delay(f'Usuario {nuevo_nombre_usuario} creado con éxito')
        except ValueError:
            imprimir_con_delay('Ingrese valores válidos.')
   
    # Implementado en Accion Registrarse
    def registrar_usuario(self):
        try:
            nuevo_nombre_usuario = input('Ingresar nombre: ')

            # Verificar si el usuario ya existe en la base de datos
            if self.db.usuario_existe(nuevo_nombre_usuario):
                imprimir_con_delay(f'El nombre "{nuevo_nombre_usuario}" ya existe. No se puede crear.')
                return  # Evita continuar si el usuario ya existe

            nueva_contraseña_usuario = input('Ingresar contraseña: ')
            nuevo_saldo_usuario = 0.0

            # Crear el usuario en la base de datos
            self.db.crear_nuevo_usuario(nuevo_nombre_usuario, nueva_contraseña_usuario, nuevo_saldo_usuario)

            # No necesitamos crear un objeto Usuario aquí, solo estamos registrando usuarios
            # El objeto Usuario se crea cuando alguien inicia sesión
            imprimir_con_delay('Registro Exitoso')
        except ValueError:
            print('Ingrese valores válidos')

    def inicializar_sistema(self):
        self.db.conectar()                     # Conectar a la base de datos
        self.db.crear_tabla_usuarios()         # Crear la tabla de usuarios si no existe
        # Si no hay usuarios en la base de datos, se crea un usuario por defecto
        if self.db.verificar_usuarios_existentes() == 0:
            self.db.crear_usuario_inicial()

    def autenticar_usuario(self):
        intentos = 3
        while intentos > 0:
            usuario = input('Ingrese su nombre de usuario: ')
            contraseña = input('Ingrese su contraseña: ')
            resultado = self.db.autenticar_usuario(usuario, contraseña)
            if resultado:
                id_usuario, saldo = resultado
                imprimir_con_delay(f'Bienvenido {usuario}')
                self._usuario_actual = Usuario(id_usuario, usuario, saldo, self.db)
                return True
            else:
                intentos -= 1
                imprimir_con_delay(f'Usuario o contraseña incorrectos. Intentos restantes: {intentos}')
        imprimir_con_delay('Demasiados intentos. Reinicie el programa e intente de nuevo.')
        return False
    
    def iniciar_sesion(self):

        intentos = 3  # Se permiten hasta 3 intentos de inicio de sesión

        while intentos > 0:
            # Pedir al usuario sus credenciales
            usuario = input('Ingrese su nombre de usuario: ')
            contraseña = input('Ingrese su contraseña: ')

            # Verificar si las credenciales son correctas
            resultado = self.db.autenticar_usuario(usuario, contraseña)

            if resultado:
                id_usuario, saldo = resultado  # Si es válido, se obtiene el ID y saldo del usuario
                imprimir_con_delay(f'Bienvenido {usuario}')
                
                # Crear un objeto Usuario con la información autenticada, el usuario autenticado para usarlo en el resto del sistema
                self._usuario_actual = Usuario(id_usuario, usuario, saldo, self.db)

                return True
            else:
                intentos -= 1  # Reducir el contador de intentos
                imprimir_con_delay(f'Usuario o contraseña incorrectos. Intentos restantes: {intentos}')
                
                if intentos == 0:
                    imprimir_con_delay('Demasiados intentos. Reinicie el programa e intente de nuevo.')
                    break
        return False

    def get_usuario_actual(self):
        return self._usuario_actual