class Graficos:

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
    
    