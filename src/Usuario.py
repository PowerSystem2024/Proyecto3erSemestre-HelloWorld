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
        try:
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            if cantidad > self.saldo:
                imprimir_con_delay('Saldo no disponible')
            else:
                imprimir_con_delay('Saldo retirado con éxito')
                self.saldo -= cantidad
                self.db.actualizar_saldo(self.id_usuario, self.saldo)
        except ValueError:
            imprimir_con_delay('Ingrese un número válido')
        return
    
    def depositar_saldo(self):
        try:
            cantidad = int(input("Ingrese la cantidad a depositar: "))
            if cantidad <= 0:
                imprimir_con_delay('Por favor ingrese una cantidad válida mayor a cero')
            else:
                self.saldo += cantidad
                self.db.actualizar_saldo(self.id_usuario, self.saldo)
                imprimir_con_delay(f'Se depositaron {cantidad} exitosamente')
                imprimir_con_delay(f'Nuevo saldo: {self.saldo}')
        except ValueError:
            imprimir_con_delay('Ingrese un número válido')
        
        return self.saldo