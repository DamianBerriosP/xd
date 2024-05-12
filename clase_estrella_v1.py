import numpy as np
class Estrella(): # Clase estrella
    """
    Clase que representa una estrella. Sus atributos principales son:

    Atributos:
    - nombre: El nombre de la estrella. (público)
    - masa: La masa de la estrella. (protegido)
    - radio: El radio de la estrella. (protegido)
    - temperaturasuperficial: La temperatura superficial de la estrella. (protegido)
    - distancia: La distancia de la estrella. (protegido)
    - movimientopropio: El movimiento propio de la estrella. (protegido)
    """

    def __init__(self, name, mass, radius, surfacetemperature, distance, ownmovement): # Constructor
        self.nombre = name
        self._masa = mass
        self._radio = radius
        self._teff= surfacetemperature
        self._distancia = distance
        self._movimiento= ownmovement
    
    def luminosidad_total(self): # Método
        """
        Calcula la luminosidad total de la estrella.

        Returns:
        - Retornara la luminosidad total de la estrella.
        """
        return float(4 * np.pi * (self._radio**2) * self._teff)
    
    def luminosidad_secuencia_principal(self,sun_luminosity, sun_mass):# Método
        """
        Calcula la luminosidad de la estrella en la secuencia principal.

        Parámetros:
        - sun_luminosity: La luminosidad del Sol.
        - sun_mass: La masa del Sol.

        Returns:
        - Retorna la luminosidad de la estrella en la secuencia principal.
        """
        return  float( sun_luminosity * (self._masa/sun_mass)**3.5)
    
    
    # Funciones nuevas:

def movimiento_absoluto(self):
        """
        Calcula el movimiento absoluto de la estrella.

        Returns:
        - El movimiento absoluto de la estrella.
        """
        return float(self._movimiento / self._distancia)



def brillo_aparente(self):
        """
        Calcula el brillo aparente de la estrella.

        Returns:
        - El brillo aparente de la estrella.
        """
        luminosidad = self.luminosidad_total()
        return float(luminosidad / (4 * np.pi * self._distancia**2))