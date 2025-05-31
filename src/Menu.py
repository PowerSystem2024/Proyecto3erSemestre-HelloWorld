from .Graficos import Graficos
from .Accion import Accion
from .utilidades import escribir_con_retraso, borrar_pantalla

class Menu:

    MAX_OPCIONES_VISIBLES = 8
    NUMERO_FILAS_MENU = 4
    NUMERO_COLUMNAS_MENU = 2
    ALTURA_GENERAL_CELDA = 5
    ANCHO_CELDA_RECTANGULAR = 28
    ALTO_CELDA_RECTANGULAR = ALTURA_GENERAL_CELDA
    ANCHO_CELDA_NUMERICA = 12
    ALTO_CELDA_NUMERICA = ALTURA_GENERAL_CELDA
    ANCHO_CELDA_FLECHA = 24
    ALTO_CELDA_FLECHA = ALTURA_GENERAL_CELDA
    ESPACIO_ENTRE_FILAS_MENU = 4
    ESPACIO_ENTRE_COLUMNAS_MENU = 2
    
    # Instancias de Celdas Básicas y Gráficos
    GRAFICOS_CELDA_RECTANGULAR = Graficos(ANCHO_CELDA_RECTANGULAR, ALTO_CELDA_RECTANGULAR)
    GRAFICOS_CELDA_NUMERICA = Graficos(ANCHO_CELDA_NUMERICA, ALTO_CELDA_NUMERICA)
    GRAFICOS_CELDA_FLECHA = Graficos(ANCHO_CELDA_FLECHA, ALTO_CELDA_FLECHA)

    CELDA_RECTANGULAR = GRAFICOS_CELDA_RECTANGULAR.crear_celda_rectangular()
    CELDA_RECTANGULAR_VACIA = GRAFICOS_CELDA_RECTANGULAR.crear_celda_rectangular_vacia()

    CELDA_NUMERICA = GRAFICOS_CELDA_NUMERICA.crear_celda_numerica()
    CELDA_NUMERICA_VACIA = GRAFICOS_CELDA_NUMERICA.crear_celda_numerica_vacia()

    CELDA_FLECHA_IZQUIERDA = GRAFICOS_CELDA_FLECHA.crear_celda_flecha_izquierda()
    CELDA_FLECHA_DERECHA = GRAFICOS_CELDA_FLECHA.crear_celda_flecha_derecha()
    CELDA_FLECHA_VACIA = GRAFICOS_CELDA_FLECHA.crear_celda_flecha_vacia()


    def __init__(self, acciones):
        """
        Inicializa una instancia de la clase Menu.

        Parámetros:
            - acciones: lista de listas, donde cada sublista contiene clases que representan
                        acciones disponibles en una sección del menú.
        """
        self._indice_actual = 0
        self._validar_estructura_acciones(acciones)
        self._validar_limite_opciones_visibles(acciones)
        self._validar_acciones(acciones)
        self._acciones = acciones

    def _validar_estructura_acciones(self, acciones):
        if not all(isinstance(grupo_acciones, list) for grupo_acciones in acciones):
            raise TypeError("El parámetro 'acciones' debe ser una lista de listas.")

    def _validar_limite_opciones_visibles(self, acciones):
        for grupo_acciones in acciones:
            if len(grupo_acciones) > self.MAX_OPCIONES_VISIBLES:
                raise ValueError(f"Cada grupo de instancias de Acciones debe tener como máximo {self.MAX_OPCIONES_VISIBLES} acciones.")
            elif len(grupo_acciones) < 1:
                raise ValueError(f"Cada grupo de instancias de Acciones debe tener como mínimo al menos una acción.")

    
    def _validar_acciones(self, acciones):
        for grupo_acciones in acciones:
            for accion_instancia in grupo_acciones:
                if not isinstance(accion_instancia, Accion):
                    raise TypeError("Cada instancia debe ser de una clase que herede de 'Accion'.")
                if not hasattr(accion_instancia, "obtener_nombre") or not callable(getattr(accion_instancia, "obtener_nombre")):
                    raise TypeError("Cada clase en 'Acciones' debe implementar el método 'obtener_nombre'.")
                if not hasattr(accion_instancia, "ejecutar") or not callable(getattr(accion_instancia, "ejecutar")):
                    raise TypeError("Cada clase en 'Acciones' debe implementar el método 'ejecutar'.")

    def get_indice_actual(self):
        return self._indice_actual

    def set_indice_actual(self, nuevo_indice):
        self._indice_actual = nuevo_indice

    def get_acciones(self):
        return self._acciones



    def _insertar_contenido_en_celda(self, contenido, celda):
        """
        Inserta un nombre de función (usando obtener_nombre()) o un número centrado
        verticalmente y horizontalmente dentro de una celda representada por una lista de cadenas.

        Parámetros:
            - contenido: una instancia de una clase en 'Acciones' con método obtener_nombre() o un número entero.
            - celda: lista de cadenas que representan la celda.

        Retorna:
            - La lista de cadenas modificada con el contenido insertado.
        """
        if isinstance(contenido, Accion):
            texto = str(contenido.obtener_nombre())
        elif isinstance(contenido, int):
            texto = str(contenido)
        else:
            raise TypeError("El contenido debe ser una función con obtener_nombre() o un número entero.")

        alto = len(celda)
        if alto == 0:
            return celda

        ancho = len(celda[0])
        if ancho == 0:
            return celda
        
        indice_central = alto // 2

        linea = celda[indice_central]
        borde_izquierdo = linea[0]
        borde_derecho = linea[-1]
        espacio_interno = ancho - 2
        
        if espacio_interno < len(texto) + 2:
            raise ValueError("La celda es demasiado angosta para insertar el texto con padding mínimo.")

        texto_centrado = texto.center(espacio_interno)
        nueva_linea = f"{borde_izquierdo}{texto_centrado}{borde_derecho}"

        celda_modificada = celda.copy()

        celda_modificada[indice_central] = nueva_linea

        return celda_modificada

    def _validar_constantes_menu(self):
        if self.MAX_OPCIONES_VISIBLES < 1:
            raise ValueError("MAX_OPCIONES_VISIBLES debe ser como mínimo igual a 1.")
        if self.MAX_OPCIONES_VISIBLES % 2 != 0:
            raise ValueError("MAX_OPCIONES_VISIBLES debe ser un número par.")
        if self.MAX_OPCIONES_VISIBLES // 2 != self.NUMERO_FILAS_MENU:
            raise ValueError("MAX_OPCIONES_VISIBLES debe ser el doble de NUMERO_FILAS_MENU.")


    def _renderizar_menu_visible(self, grupo_acciones):
        
        celdas_con_opciones = []
        celdas_con_numeros = []
        celdas_con_flechas = []
        filas_menu = []
        i = 0
        numero_opciones = len(grupo_acciones)

        for accion_instancia in grupo_acciones:
            celdas_con_opciones.append(self._insertar_contenido_en_celda(accion_instancia, self.CELDA_RECTANGULAR))

        for numero_opcion in range(numero_opciones):
            celdas_con_numeros.append(self._insertar_contenido_en_celda(numero_opcion + 1, self.CELDA_NUMERICA))
            if (numero_opcion % 2 == 0):
                celdas_con_flechas.append(self.CELDA_FLECHA_IZQUIERDA)
            else:
                celdas_con_flechas.append(self.CELDA_FLECHA_DERECHA)
        
        if numero_opciones < self.MAX_OPCIONES_VISIBLES:
            for numero_opcion_restante in range(numero_opciones, self.MAX_OPCIONES_VISIBLES):
                celdas_con_opciones.append(self.CELDA_RECTANGULAR_VACIA)
                celdas_con_numeros.append(self.CELDA_NUMERICA_VACIA)
                celdas_con_flechas.append(self.CELDA_FLECHA_VACIA)
        
        for fila_celda_menu in range(self.NUMERO_FILAS_MENU):
            for fila_celda in range(Menu.ALTURA_GENERAL_CELDA):
                filas_menu.append(
                                    f"{celdas_con_numeros[i][fila_celda]}"
                                    f"{celdas_con_flechas[i][fila_celda]}"
                                    f"{celdas_con_opciones[i][fila_celda]}"
                                    f"{Graficos.ESPACIO * Menu.ESPACIO_ENTRE_COLUMNAS_MENU}"
                                    f"{celdas_con_opciones[i + 1][fila_celda]}"
                                    f"{celdas_con_flechas[i + 1][fila_celda]}"
                                    f"{celdas_con_numeros[i + 1][fila_celda]}"
                                )
            for linea_vacia in range(Menu.ESPACIO_ENTRE_FILAS_MENU):
                filas_menu.append("")
            i += 2
        
        for fila in filas_menu:
            escribir_con_retraso(fila)
        
    def _seleccionar_opcion_menu_visible(self, grupo_acciones):
        numero_opciones = len(grupo_acciones)
        try:
            opcion_elegida = int(input(f"Elegir una opción: "))
            if 1 <= opcion_elegida <= numero_opciones:
                return opcion_elegida - 1  # Ajustar para índices que comienzan en 0
        except ValueError:
            pass  # Entrada no válida, se ignora

        return None  # Indica que no se seleccionó una opción válida


    def crear_menu(self):
        borrar_pantalla()
        self._validar_constantes_menu()

        while True:
            i = self.get_indice_actual()
            self._renderizar_menu_visible(self._acciones[i])

            opcion_elegida = self._seleccionar_opcion_menu_visible(self._acciones[i])
            if opcion_elegida is None:
                continue

            accion = self._acciones[i][opcion_elegida]
            es_accion_salir_volver = accion.ejecutar(self)

            if es_accion_salir_volver:
                break

            