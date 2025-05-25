
from abc import ABC, abstractmethod
from datetime import *
from centro_de_salud import Centro_Salud


class Paciente(ABC):


    def __init__(self, nombre: str, dni: int, fecha_nac: str, sexo: str, tel: str, t_sangre: str, centro_salud: Centro_Salud):
        """
        IMPORTANTE: hacer una funcion para pedir datos, y adentro de ahi
        """
        self._nombre = nombre
        self._dni = dni
        self._fecha_nac = fecha_nac
        self._sexo = sexo
        self.tel = tel
        self._t_sangre = t_sangre
        self.centro_salud = centro_salud
    

    def get_nombre(self):
        return self._nombre
    def get_dni(self):
        return self._dni
    def get_fecha_nac(self):
        return self._fecha_nac
    def get_sexo(self):
        return self._sexo
    def get_t_sangre(self):
        return self._t_sangre

    def set_nombre(self, nombre: str):
        self._nombre = nombre
    def set_dni(self, dni: int):
        self._dni = dni
    def set_fecha_nac(self, fecha_nac: str):
        self._fecha_nac = fecha_nac
    def set_sexo(self, sexo: str):
        self._sexo = sexo
    def set_t_sangre(self, t_sangre: str):
        self._t_sangre = t_sangre
    @abstractmethod
    def __repr__(self):
        pass
    

