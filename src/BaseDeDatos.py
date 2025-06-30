# base_de_datos.py
import sqlite3

class BaseDeDatos:
    def __init__(self, db_name='cajero.db'):
        # Inicializa la clase con el nombre de la base de datos
        self.db_name = db_name
        self.conexion = None
        self.cursor = None

    def conectar(self):
        # Establece la conexión con la base de datos
        self.conexion = sqlite3.connect(self.db_name)
        self.cursor = self.conexion.cursor()

    def crear_tabla_usuarios(self):
        # Crea la tabla de usuarios si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                contraseña TEXT NOT NULL,
                saldo REAL DEFAULT 0
            )
        ''')

    def verificar_usuarios_existentes(self):
        # Verifica si hay usuarios registrados en la base de datos
        self.cursor.execute('SELECT COUNT(*) FROM usuarios')
        return self.cursor.fetchone()[0]

    def usuario_existe(self, nombre_usuario):
        # Verifica si un nombre de usuario ya existe
        self.cursor.execute('SELECT COUNT(*) FROM usuarios WHERE nombre = ?', (nombre_usuario,))
        return self.cursor.fetchone()[0] > 0

    def crear_nuevo_usuario(self, nombre, contraseña, saldo_inicial=0.0):
        # Inserta un nuevo usuario en la base de datos
        self.cursor.execute(
            'INSERT INTO usuarios (nombre, contraseña, saldo) VALUES (?, ?, ?)',
            (nombre, contraseña, saldo_inicial)
        )
        self.conexion.commit()

    def crear_usuario_inicial(self):
        # Crea un usuario inicial por defecto si la tabla está vacía
        self.cursor.execute(
            'INSERT INTO usuarios (nombre, contraseña, saldo) VALUES (?, ?, ?)',
            ('joaquin', '1234', 1000.0)
        )
        self.conexion.commit()

    def autenticar_usuario(self, usuario, contraseña):
        # Verifica las credenciales del usuario para iniciar sesión
        self.cursor.execute('SELECT id, saldo FROM usuarios WHERE nombre = ? AND contraseña = ?', 
                            (usuario, contraseña))
        return self.cursor.fetchone()

    def actualizar_saldo(self, id_usuario, nuevo_saldo):
        # Actualiza el saldo de un usuario específico
        self.cursor.execute('UPDATE usuarios SET saldo = ? WHERE id = ?', (nuevo_saldo, id_usuario))
        self.conexion.commit()

    def obtener_usuarios(self):
        # Devuelve una lista de los nombres de todos los usuarios registrados
        self.cursor.execute('SELECT nombre FROM usuarios ORDER BY nombre')
        return [row[0] for row in self.cursor.fetchall()]

    def cerrar_conexion(self):
        # Cierra la conexión con la base de datos si está abierta
        if self.conexion:
            self.conexion.close()

    def obtener_id_saldo_por_nombre(self, nombre_usuario):
        self.cursor.execute('SELECT id, saldo FROM usuarios WHERE nombre = ?', (nombre_usuario,))
        return self.cursor.fetchone()  # Devuelve (id, saldo) o None
