from .BaseDeDatos import BaseDeDatos
from .Utilidades import *
from .Usuario import Usuario
from .RespuestaSemantica import RespuestaSemantica

class Cajero:
    def __init__(self):
        self.db = BaseDeDatos()                # Crear instancia de la base de datos
        self._usuario_actual = None
        self._intentos_fallidos = {}
    

    def terminar_programa(self) -> dict:
        self.db.cerrar_conexion()
        return RespuestaSemantica(tipo_respuesta="terminar_programa") \
            .con_exito() \
            .obtener_diccionario()

    
    def mostrar_usuarios_registrados(self) -> dict:
        respuesta = RespuestaSemantica(
            tipo_respuesta="mostrar_usuarios_registrados"
        )

        usuarios = self.db.obtener_usuarios()

        if not usuarios:
            return respuesta.con_error("sin_usuarios_registrados").obtener_diccionario()

        return respuesta.con_exito({
            "usuarios": usuarios
        }).obtener_diccionario()

    
    def generar_usuario(self, nombre_usuario: str, contraseña: str, saldo_inicial) -> dict:
        respuesta = RespuestaSemantica(tipo_respuesta="generar_usuario")

        # Validar datos de usuario
        valido, resultado = validar_datos_usuario(nombre_usuario, contraseña, saldo_inicial)
        if not valido:
            return respuesta.con_error(resultado).obtener_diccionario()
        
        nombre_usuario, contraseña, saldo_inicial = resultado  # Datos ya validados y tipados

        # Verificar existencia del usuario
        if self.db.usuario_existe(nombre_usuario):
            return respuesta.con_error("usuario_ya_existe").obtener_diccionario()

        # Crear usuario
        self.db.crear_nuevo_usuario(nombre_usuario, contraseña, saldo_inicial)
        return respuesta.con_exito({
            "nombre_usuario": nombre_usuario,
            "saldo_inicial": saldo_inicial
        }).obtener_diccionario()


   
    def registrar_usuario(self, nombre_usuario: str, contraseña: str) -> dict:
        respuesta = RespuestaSemantica(tipo_respuesta="registrar_usuario")
        
        # Validar datos del usuario
        valido, error = validar_datos_usuario(nombre_usuario, contraseña, saldo=0.0)
        if not valido:
            return respuesta.con_error(error).obtener_diccionario()

        # Verificar existencia
        if self.db.usuario_existe(nombre_usuario):
            return respuesta.con_error("usuario_ya_existe").obtener_diccionario()

        # Crear usuario con saldo inicial 0.0
        self.db.crear_nuevo_usuario(nombre_usuario, contraseña, 0.0)

        return respuesta.con_exito({
            "nombre_usuario": nombre_usuario,
            "saldo_inicial": 0.0
        }).obtener_diccionario()


    def inicializar_sistema(self):
        self.db.conectar()                     # Conectar a la base de datos
        self.db.crear_tabla_usuarios()         # Crear la tabla de usuarios si no existe
        # Si no hay usuarios en la base de datos, se crea un usuario por defecto
        if self.db.verificar_usuarios_existentes() == 0:
            self.db.crear_usuario_inicial()

    def _autenticar_usuario(self, nombre_usuario: str, contraseña: str) -> Usuario | None:
        resultado = self.db.autenticar_usuario(nombre_usuario, contraseña)
        if resultado:
            id_usuario, saldo = resultado
            return Usuario(id_usuario, nombre_usuario, saldo, self.db)
        return None


    def iniciar_sesion(self, nombre_usuario, contraseña) -> dict:
        respuesta = RespuestaSemantica(tipo_respuesta="iniciar_sesion")
        max_intentos = 3

        intentos = self._intentos_fallidos.get(nombre_usuario, 0)
        if intentos >= max_intentos:
            return respuesta.con_error("demasiados_intentos").obtener_diccionario()

        usuario = self._autenticar_usuario(nombre_usuario, contraseña)
        if usuario:
            self._usuario_actual = usuario
            self._intentos_fallidos[nombre_usuario] = 0
            return respuesta.con_exito({
                "id_usuario": usuario.id_usuario,
                "nombre_usuario": usuario.nombre,
                "saldo": usuario.saldo
            }).obtener_diccionario()
        else:
            self._intentos_fallidos[nombre_usuario] = intentos + 1
            return respuesta.con_error("credenciales_invalidas").obtener_diccionario()



    def obtener_usuario_actual(self):
        return self._usuario_actual