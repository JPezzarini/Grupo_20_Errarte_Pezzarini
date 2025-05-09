from datetime import *
from enum import Enum

class Tipo(Enum):
    corazón = 1
    pulmón = 2
    piel = 3
    córnea = 4
    hueso = 5
    intestino = 6
    riñon = 7
    hígado = 8
    páncreas = 9

class Organo():


    def __init__(self, tipo: Tipo):
        self._tipo = tipo
        self.dt_hablacion = None


