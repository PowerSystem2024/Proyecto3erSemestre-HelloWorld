from .utilidades import imprimir_con_delay

class Usuario:
    def __init__(self, id_usuario, nombre, saldo, db):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.saldo = saldo
        self.db = db
    
    
    def consultar_saldo(self):
        imprimir_con_delay(f'Su saldo disponible es de: {self.saldo}')
    

    def retirar_saldo(self):
        entrada = input("Ingrese la cantidad a retirar: ")
        try:
            cantidad = int(entrada)
            if cantidad <= 0:
                imprimir_con_delay("La cantidad debe ser mayor que cero.")
                return
            if cantidad > self.saldo:
                imprimir_con_delay('Saldo no disponible')
            else:
                imprimir_con_delay('Saldo retirado con éxito')
                self.saldo -= cantidad
                self.db.actualizar_saldo(self.id_usuario, self.saldo)
        except ValueError:
                imprimir_con_delay("Debe ingresar un número válido (sin letras ni símbolos).")
        return self.saldo
    

    def depositar_saldo(self):
        entrada = input("Ingrese la cantidad a depositar: ")
        try:
            cantidad = int(entrada)
            if cantidad <= 0:
                imprimir_con_delay("La cantidad debe ser mayor que cero.")
                return
            else:
                self.saldo += cantidad
                self.db.actualizar_saldo(self.id_usuario, self.saldo)
                imprimir_con_delay(f'Se depositaron {cantidad} exitosamente')
                imprimir_con_delay(f'Nuevo saldo: {self.saldo}')
        except ValueError:
            imprimir_con_delay("Debe ingresar un número válido (sin letras ni símbolos).")
        return self.saldo
    

    def transferir_saldo(self):
        entrada = input("Ingrese la cantidad a transferir: ")
        try:
            cantidad = int(entrada)
            if cantidad <= 0:
                imprimir_con_delay("La cantidad debe ser mayor que cero.")
                return
            elif cantidad > self.saldo:
                imprimir_con_delay('Saldo no disponible')
                return
            else:
                nombre_destino = input("Ingrese el nombre del usuario a transferir: ")
                if nombre_destino == self.nombre:
                    imprimir_con_delay("No puede transferirse saldo a usted mismo.")
                    return self.saldo

                if not self.db.usuario_existe(nombre_destino):
                    imprimir_con_delay("El usuario destino no existe.")
                    return self.saldo
                
                resultado = self.db.obtener_id_saldo_por_nombre(nombre_destino)
                if resultado is None:
                    imprimir_con_delay("Error interno: no se encontró el usuario destino.")
                    return self.saldo
                
                id_destino, saldo_destino = resultado

                self.saldo -= cantidad
                nuevo_saldo_destino = saldo_destino + cantidad

                self.db.actualizar_saldo(self.id_usuario, self.saldo)
                self.db.actualizar_saldo(id_destino, nuevo_saldo_destino)

                imprimir_con_delay('Saldo transferido con éxito.')
                
        except ValueError:
            imprimir_con_delay("Debe ingresar un número válido (sin letras ni símbolos).")
        return self.saldo
    

    def get_nombre(self):
        return self.nombre