from .utilidades import validar_valor_positivo, validar_valor_no_negativo, validar_usuario
from .RespuestaSemantica import RespuestaSemantica

class Usuario:
    def __init__(self, id_usuario, nombre, saldo, db):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.saldo = saldo
        self.db = db
    
    def consultar_saldo(self):
        respuesta = RespuestaSemantica(
            tipo_respuesta="consultar_saldo", 
            nombre="Consultar Saldo"
        )

        valido, error = validar_valor_no_negativo(self.saldo)
        if not valido:
            return respuesta.con_error(error).obtener_diccionario()

        return respuesta.con_exito({
            "id_usuario": self.id_usuario,
            "saldo_actual": self.saldo
        }).obtener_diccionario()

        
    
    def retirar_dinero(self, cantidad) -> dict:
        respuesta = RespuestaSemantica(
            tipo_respuesta="retirar_dinero",
            nombre="Retirar Dinero"
        )

        valido, resultado = validar_valor_positivo(cantidad)
        if not valido:
            return respuesta.con_error(resultado).obtener_diccionario()
        cantidad = resultado

        valido, error = validar_valor_no_negativo(self.saldo)
        if not valido:
            return respuesta.con_error(error).obtener_diccionario()

        if cantidad > self.saldo:
            return respuesta.con_error("saldo_insuficiente").obtener_diccionario()

        self.saldo -= cantidad
        self.db.actualizar_saldo(self.id_usuario, self.saldo)

        return respuesta.con_exito({
            "id_usuario": self.id_usuario,
            "saldo_actual": self.saldo,
            "monto_retirado": cantidad
        }).obtener_diccionario()


    
    def depositar_dinero(self, cantidad) -> dict:
        respuesta = RespuestaSemantica(
            tipo_respuesta="depositar_dinero",
            nombre="Depositar Dinero"
        )

        valido, resultado = validar_valor_positivo(cantidad)
        if not valido:
            return respuesta.con_error(resultado).obtener_diccionario()
        cantidad = resultado

        valido, error = validar_valor_no_negativo(self.saldo)
        if not valido:
            return respuesta.con_error(error).obtener_diccionario()

        self.saldo += cantidad
        self.db.actualizar_saldo(self.id_usuario, self.saldo)

        return respuesta.con_exito({
            "id_usuario": self.id_usuario,
            "monto_depositado": cantidad,
            "saldo_actual": self.saldo
        }).obtener_diccionario()

    
    def transferir_dinero(self, cantidad, usuario_destino) -> dict:
        respuesta = RespuestaSemantica(
            tipo_respuesta="transferir_dinero",
            nombre="Transferir Dinero"
        )

        # Validar cantidad
        valido, resultado = validar_valor_positivo(cantidad)
        if not valido:
            return respuesta.con_error(resultado).obtener_diccionario()
        cantidad = resultado

        # Validar saldo del usuario origen
        valido, error = validar_valor_no_negativo(self.saldo)
        if not valido:
            return respuesta.con_error(error).obtener_diccionario()

        if cantidad > self.saldo:
            return respuesta.con_error("saldo_insuficiente").obtener_diccionario()

        # Validar destinatario
        valido, error = validar_usuario(usuario_destino)
        if not valido:
            return respuesta.con_error(error).obtener_diccionario()


        # Validar que no sea el mismo usuario
        if self.id_usuario == usuario_destino.id_usuario:
            return respuesta.con_error("transferencia_a_mismo_usuario").obtener_diccionario()

        # Realizar transferencia
        self.saldo -= cantidad
        usuario_destino.saldo += cantidad

        self.db.actualizar_saldo(self.id_usuario, self.saldo)
        usuario_destino.db.actualizar_saldo(usuario_destino.id_usuario, usuario_destino.saldo)

        return respuesta.con_exito({
            "id_usuario_origen": self.id_usuario,
            "id_usuario_destino": usuario_destino.id_usuario,
            "monto_transferido": cantidad,
            "saldo_origen": self.saldo,
            "saldo_destino": usuario_destino.saldo
        }).obtener_diccionario()

    
    def obtener_nombre(self):
        return self.nombre