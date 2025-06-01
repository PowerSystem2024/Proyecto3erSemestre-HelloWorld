from abc import ABC, abstractmethod

class Accion(ABC):
    """
    Clase abstracta base para representar una acción en el sistema.

    Esta clase define una interfaz común para todas las acciones que pueden
    ser ejecutadas desde el menú del cajero. Cada acción debe proporcionar
    un nombre identificador y definir su comportamiento mediante la implementación
    del método abstracto 'ejecutar'.

    Atributos:
        _nombre (str): Nombre de la acción. Se utiliza para mostrar el texto asociado
                       en el menú.

    Métodos:
        obtener_nombre() -> str:
            Retorna el nombre de la acción.

        ejecutar():
            Método abstracto que debe ser implementado por todas las subclases.

        es_control() -> bool:
            Indica si la acción es un controlador de navegación.

        accion_menu(menu):
            Define cómo debe modificarse el menú si la acción es de control.
    """

    def __init__(self, nombre):
        """
        Inicializa una acción con su nombre identificador.

        Parámetros:
            nombre (str): Texto que representa el nombre de la acción.
        """
        self._nombre = nombre

    def obtener_nombre(self):
        """
        Retorna el nombre de la acción.

        Retorna:
            str: Nombre con el que se identifica la acción.
        """
        return self._nombre

    # Arreglar Docs
    @abstractmethod
    def ejecutar(self, menu):
        """
        Método abstracto que representa la ejecución de la acción.

        Modifica el estado del menú cuando necesario.

        Este método puede ser sobrescrito por subclases para cambiar el comportamiento
        del menú (por ejemplo, avanzar de página o salir).

        Parámetros:
            menu: Referencia al menú actual.

        Este método debe ser implementado obligatoriamente por cualquier clase
        que herede de 'Accion'.

        Lanza:
            NotImplementedError: Si no es implementado por una subclase.
        """
        pass

