import numpy as np
class Planeta():
    """
    Clase que representa un planeta que orbita alrededor de una estrella. Un planeta es un cuerpo con masa menor que 13 Mjup (masas de Júpiter) que orbita una estrella. 
    Los atributos principales de un planeta son:
    
    Atributos:
    - nombre: El nombre del planeta.
    - estrella_protegida: La estrella alrededor de la cual orbita el planeta.
    - masaplanetaria: La masa del planeta en masas de Júpiter.
    - radio: El radio del planeta.
    - a: El semieje mayor de la órbita del planeta.
    - i: La inclinación de la órbita del planeta.
    - e: La excentricidad de la órbita del planeta.
    - periastron: El argumento del periastron del planeta.
    """
    def __init__(self, nombre, estrella_protegida, masaplanetaria, radio, a, i, e, periastron):
        self._nombre= nombre
        self._estrella_protegida= estrella_protegida
        self._masaplanetaria= masaplanetaria
        self._radio= radio
        self._a= a # semieje mayor
        self._i= i # inclinación
        self._e= e # excentricidad
        self._w= periastron # argumento del periastron

    def periodo_rotacion_kepleriana(self,g):
        """
        Calcula y devuelve el periodo de rotación kepleriano del planeta.
        
        Parámetros:
        - g: La constante gravitacional.
        
        Retorna:
        - El periodo de rotación kepleriano del planeta como un número de punto flotante.
        """
        if self._masaplanetaria != 0 and self._a != 0:
            return float(2*np.pi*np.sqrt((self._a**3)/(g*self._masaplanetaria)))
        else:
            return 0

    # Funciones nuevas:

    def tipo_planeta(self):
        """
        Clasifica el tipo de planeta en función de su masa y radio.
        Retorna:
        - El tipo de planeta como una cadena de texto.
        """
        if self._masaplanetaria < 0.1 and self._radio < 1.5: # Asumiendo que la masa esta en masas de Júpiter y el radio en radios de Júpiter
            return "Planeta Terrestre"
        elif self._masaplanetaria < 13 and self._radio < 4: # Pueden ser gasosos o terrestres, debido a que con las características dadas no se puede determinar con exactitud
            return "Planeta Gaseoso" "o" "Planeta Terrestre"
        elif self._masaplanetaria < 13 and self._radio >= 4:
            return "Gigante de Hielo"
        else:
            return "Otro"