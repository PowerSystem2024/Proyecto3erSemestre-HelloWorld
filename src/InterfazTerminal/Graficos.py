class Graficos:
    """
    Clase encargada de generar representaciones gráficas en forma de celdas de texto.

    Permite construir celdas rectangulares con bordes personalizados y celdas con flechas horizontales
    centradas (hacia la izquierda o la derecha), usando caracteres ASCII.

    Las dimensiones de las celdas se definen al crear la instancia. 
    Los métodos disponibles permiten crear:

    - Celdas rectangulares.
    - Celdas con formato numérico (requieren ancho y alto iguales).
    - Celdas con flechas horizontales, centradas verticalmente.
    - Celdas vacías de los otros tipos de celdas.

    Atributos:
        - ancho_celda (int): define el ancho de todas las celdas generadas.
        - alto_celda (int): define el alto de todas las celdas generadas.

    Uso:
        graficos = Graficos(ancho, alto)
        celda = graficos.crear_celda_rectangular()
        flecha = graficos.crear_flecha_izquierda()
    """


    def __init__(self, ancho_celda, alto_celda):
        if ancho_celda < 3:
            raise ValueError("El ancho de la celda debe ser al menos 3.")
        if alto_celda < 3:
            raise ValueError("El alto de la celda debe ser al menos 3.")
        if alto_celda % 2 == 0:
            raise ValueError("El alto de la celda debe ser un número impar.")
        self._ancho_celda = ancho_celda
        self._alto_celda = alto_celda

    PUNTO = '.'
    IGUAL = '='
    BARRA_VERTICAL = '|'
    MAYOR = '>'
    MENOR = '<'
    GUION = '-'
    ESPACIO = ' '


    def _crear_celda(self, extremo_esquina, extremo_lateral, intermedio, ancho, alto):
        
        """
        Crea una celda con bordes definidos por los caracteres recibidos.

        Parámetros:
            - extremo_esquina: caracter para las esquinas (ejemplo: '.')
            - extremo_lateral: caracter para los bordes verticales (ejemplo: '|')
            - intermedio: caracter para los bordes horizontales (ejemplo: '=')
            - ancho: ancho total de la celda (incluye esquinas y bordes)
            - alto: alto total de la celda (incluye bordes superior e inferior)

        Retorna:
            - Lista de strings, cada uno representa una línea de la celda.
        """

        # Línea superior: esquina + intermedio * (ancho - 2) + esquina
        linea_superior = extremo_esquina + intermedio * (ancho - 2) + extremo_esquina
        # Líneas internas: borde lateral + espacios + borde lateral
        linea_interna = extremo_lateral + self.ESPACIO * (ancho - 2) + extremo_lateral
        # Línea inferior igual a la superior
        linea_inferior = linea_superior

        celda = [linea_superior]
        for _ in range(alto - 2):
            celda.append(linea_interna)
        celda.append(linea_inferior)

        return celda
    

    def crear_celda_rectangular(self):
        """
        Crea una celda rectangular con bordes definidos por los caracteres de la clase.

        Retorna:
            - lista de strings: representa las líneas de la celda con el ancho y alto definidos
                                por los atributos de la instancia.
        """

        if self._ancho_celda < self._alto_celda:
            raise ValueError("Para la celda rectangular, el ancho debe ser mayor que el alto.")

        return self._crear_celda(self.PUNTO, self.BARRA_VERTICAL, self.IGUAL, self._ancho_celda, self._alto_celda)
    

    def crear_celda_rectangular_vacia(self):
        """
        Crea una celda rectangular vacía.

        Retorna:
            - lista de strings: representa las líneas de la celda con el ancho y alto definidos
                                por los atributos de la instancia.
        """
        
        if self._ancho_celda < self._alto_celda:
            raise ValueError("Para la celda rectangular, el ancho debe ser mayor que el alto.")


        return self._crear_celda(self.ESPACIO, self.ESPACIO, self.ESPACIO, self._ancho_celda, self._alto_celda)
    
    
    def crear_celda_numerica(self):

        """
        Crea una celda con formato numérico utilizando los atributos
        de ancho y alto definidos en la instancia.

        Retorna:
            - lista de strings: cada string representa una línea de la celda.
        """

        return self._crear_celda(self.PUNTO, self.BARRA_VERTICAL, self.IGUAL, self._ancho_celda, self._alto_celda)
    

    def crear_celda_numerica_vacia(self):

        """
        Crea una celda con formato numérico vacío utilizando los atributos
        de ancho y alto definidos en la instancia.

        Retorna:
            - lista de strings: cada string representa una línea de la celda.
        """

        return self._crear_celda(self.ESPACIO, self.ESPACIO, self.ESPACIO, self._ancho_celda, self._alto_celda)


    def _crear_celda_flecha(self, extremo_izquierdo, extremo_derecho):
        """
        Crea una celda con una flecha horizontal centrada.

        Usa caracteres específicos para los extremos y el cuerpo de la flecha.
        Esta función es utilizada internamente por métodos específicos para cada dirección.

        Retorna:
            - Lista de strings que representan las líneas de la celda con la flecha.
        """

        # Validar dimensiones mínimas para que la flecha tenga sentido
        if self._ancho_celda < 9:
            raise ValueError("Ancho debe ser al menos 9 para crear flecha.")
        if self._ancho_celda % 3 != 0:
            raise ValueError("Ancho debe ser múltiplo de 3 para crear flecha.")

        # Construcción de la celda vacía usando el método protegido
        celda_vacia = self.crear_celda_rectangular_vacia()

        # Modificar las líneas internas para formar la flecha
        mitad = self._alto_celda // 2
        relleno = self.GUION * (self._ancho_celda // 3 - 2)  # Ajustar longitud flecha según ancho_celda
        flecha_cruda = extremo_izquierdo + relleno + extremo_derecho
        flecha = flecha_cruda.center(self._ancho_celda)  

        # Reemplazar la línea central por la flecha
        celda_flecha_centrada = celda_vacia
        celda_flecha_centrada[mitad] = flecha
        
        return celda_flecha_centrada
    

    def crear_celda_flecha_izquierda(self):

        """
        Crea una celda con una flecha horizontal centrada apuntando hacia la izquierda.

        Utiliza el carácter de menor ('<') como punta de flecha y guiones ('-') como cuerpo.
        La flecha se posiciona en el centro vertical de la celda.

        Retorna:
            - Lista de strings que representan las líneas de la celda con la flecha hacia la izquierda.
        """

        return self._crear_celda_flecha(self.MENOR, self.GUION)

    def crear_celda_flecha_derecha(self):

        """
        Crea una celda con una flecha horizontal centrada apuntando hacia la derecha.

        Utiliza guiones ('-') como cuerpo de la flecha y el carácter de mayor ('>') como punta.
        La flecha se posiciona en el centro vertical de la celda.

        Retorna:
            - Lista de strings que representan las líneas de la celda con la flecha hacia la derecha.
        """

        return self._crear_celda_flecha(self.GUION, self.MAYOR)
  
    def crear_celda_flecha_vacia(self):
        """
        Crea una celda vacía con formato de celda de flecha.

        Retorna:
            - lista de strings: representa las líneas de la celda con el ancho y alto definidos
                                por los atributos de la instancia.
        """

        if self._ancho_celda < self._alto_celda:
            raise ValueError("Para la celda flecha, el ancho debe ser mayor que el alto.")
        if self._ancho_celda < 9:
            raise ValueError("Ancho debe ser al menos 9 para crear flecha.")
        if self._ancho_celda % 3 != 0:
            raise ValueError("Ancho debe ser múltiplo de 3 para crear flecha.")

        return self._crear_celda(self.ESPACIO, self.ESPACIO, self.ESPACIO, self._ancho_celda, self._alto_celda)