
from abc import ABC, abstractmethod
from datetime import *


class Paciente(ABC):


    def __init__(self, nombre: str, DNI: int, fecha_nac: datetime, sexo: str, tel: str, t_sangre: str, centro_salud):
        """
        IMPORTANTE: hacer una funcion para pedir datos, y adentro de ahi
        """
        self._nombre = nombre
        self._DNI = DNI
        self._fecha_nac = fecha_nac
        self._sexo = sexo
        self.tel = tel
        self._t_sangre = t_sangre
        self.centro_salud = None
    
    @abstractmethod
    def __nada(self):
        pass
    

