from abc import ABC, abstractmethod

class ManejadorEntrada(ABC):
    """
    Interfaz para solicitar datos al usuario según la acción.
    """

    @abstractmethod
    def solicitar_datos(self, tipo_accion: str) -> dict:
        """
        Solicita y devuelve un diccionario con los datos necesarios para la acción.
        """
        pass

#Todo: Revisar y completar, reemplazar input por método adaptado a terminal
class ManejadorEntradaTerminal(ManejadorEntrada):
    """
    Implementación para la interfaz de consola/terminal.
    """

    def solicitar_datos(self, tipo_accion: str) -> dict:
        datos = {}

        match tipo_accion:
            case "retirar_dinero":
                cantidad = input("Ingrese la cantidad a retirar: ")
                datos["cantidad"] = cantidad

            case "iniciar_sesion":
                nombre_usuario = input("Ingrese su nombre de usuario: ")
                contraseña = input("Ingrese su contraseña: ")
                datos["nombre_usuario"] = nombre_usuario
                datos["contraseña"] = contraseña

            case "generar_usuario":
                nombre_usuario = input("Ingrese nombre de usuario nuevo: ")
                contraseña = input("Ingrese contraseña nueva: ")
                saldo_inicial = input("Ingrese saldo inicial: ")
                datos["nombre_usuario"] = nombre_usuario
                datos["contraseña"] = contraseña
                datos["saldo_inicial"] = saldo_inicial

            case "depositar_dinero":
                cantidad = input("Ingrese la cantidad a depositar: ")
                datos["cantidad"] = cantidad

            case "transferir_dinero":
                cantidad = input("Ingrese la cantidad a transferir: ")
                usuario_destino = input("Ingrese el nombre de usuario destino: ")
                datos["cantidad"] = cantidad
                datos["usuario_destino"] = usuario_destino

            case "mostrar_usuarios_registrados":
                # No se necesitan datos para esta acción
                pass

            case "terminar_programa":
                # No se necesitan datos para esta acción
                pass

            case _:
                print(f"Acción '{tipo_accion}' no reconocida o no requiere entrada de datos.")

        return datos


#Todo: Refactorizar si necesario para interfaz web
class ManejadorEntradaWeb(ManejadorEntrada):
    """
    Implementación para interfaz web.
    Aquí se reciben los datos a partir de una petición HTTP simulada con un dict.
    """

    def __init__(self, datos_peticion: dict):
        self.datos_peticion = datos_peticion

    def solicitar_datos(self, tipo_accion: str) -> dict:
        # Retorna los datos ya recibidos. Validaciones podrían agregarse.
        return self.datos_peticion