from datetime import *
from enum import Enum

class Tipo(Enum):
    """
    Esta clase enum representa los diferentes tipos de órganos disponibles para trasplante.
    Los atributos de la clase son los distintos órganos. A cada tipo se le asigna un int distinto.
    """

    corazón = 1
    pulmón = 2
    piel = 3
    córnea = 4
    hueso = 5
    intestino = 6
    riñón = 7
    hígado = 8
    páncreas = 9

class Organo():
    """
    Esta clase representa un órgano que puede ser trasplantado.
    Atributos:
        _tipo (Tipo): El tipo de órgano, representado como un valor del enum Tipo.
                      También puede inicializarse con un valor int. 
        dt_ablacion (datetime): La fecha y hora de ablación del órgano.
    """
    def __init__(self, tipo):
        if isinstance(tipo, int):
            self._tipo = Tipo(tipo)
        elif isinstance(tipo, Tipo):
            self._tipo = tipo
        self.dt_ablacion = None

    def get_tipo(self):
        """
        returns: 
            Retorna el tipo de órgano como un valor del enum Tipo
        """
        return self._tipo
    
    
