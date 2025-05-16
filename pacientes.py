
from abc import ABC, abstractmethod
from datetime import *
from centro_de_salud import Centro_Salud


class Paciente(ABC):


    def __init__(self, nombre: str, DNI: int, fecha_nac: datetime, sexo: str, tel: str, t_sangre: str, centro_salud: Centro_Salud):
        """
        IMPORTANTE: hacer una funcion para pedir datos, y adentro de ahi
        """
        self._nombre = nombre
        self._DNI = DNI
        self._fecha_nac = fecha_nac
        self._sexo = sexo
        self.tel = tel
        self._t_sangre = t_sangre
        self.centro_salud = centro_salud
    
    @abstractmethod
    def _nada(self):
        pass
    

