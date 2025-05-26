
from abc import ABC, abstractmethod
from datetime import *
from centro_de_salud import Centro_Salud


class Paciente(ABC):
    """
    Esta clase abstracta representa un paciente, que puede ser un Donante o un Receptor. 
    """

    def __init__(self, nombre: str, dni: int, fecha_nac: datetime, sexo: str, tel: str, t_sangre: str, centro_salud: Centro_Salud):
        """
        Inicializa un paciente.
        Atributos:
            - nombre (str): El nombre del paciente.
            - dni (int): El DNI del paciente.
            - fecha_nac (str): La fecha de nacimiento del paciente.
            - sexo (str): El sexo del paciente (M/F).
            - tel (str): El número de teléfono del paciente.
            - t_sangre (str): El tipo de sangre del paciente.
            - centro_salud (Centro_Salud): El centro de salud al que está asociado el paciente.
        """
        self._nombre = nombre
        self._dni = dni
        self._fecha_nac = fecha_nac
        self._sexo = sexo
        self.tel = tel
        self._t_sangre = t_sangre
        self.centro_salud = centro_salud
    

    def get_nombre(self) -> str:
        """
        Retorna el nombre del paciente.
        returns:
            Un str que indica el nombre del paciente.
        """
        return self._nombre
    def get_dni(self) -> int:
        """
        Retorna el DNI del paciente.
        returns:
            Un int que indica el DNI del paciente.
        """
        return self._dni
    def get_fecha_nac(self) -> datetime:
        """
        Retorna la fecha de nacimiento del paciente.
        returns:
            Un objeto datetime que indica la fecha de nacimiento del paciente.
        """
        return self._fecha_nac
    def get_sexo(self) -> str:
        """
        Retorna el sexo del paciente.
        returns:
            Un str que indica el sexo del paciente.
        """
        return self._sexo
    def get_t_sangre(self) -> str:
        """
        Retorna el tipo de sangre del paciente.
        returns:
            Un str que indica el tipo de sangre del paciente.
        """
        return self._t_sangre

    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre del paciente.
        params:
            - nombre: El nuevo nombre del paciente.
        """
        self._nombre = nombre
    def set_dni(self, dni: int) -> None:
        """
        Establece el DNI del paciente.
        params:
            - dni: El nuevo DNI del paciente.
        """
        self._dni = dni
    def set_fecha_nac(self, fecha_nac: str) -> None:
        """
        Establece la fecha de nacimiento del paciente.
        params:
            - fecha_nac: La nueva fecha de nacimiento del paciente.
        """
        self._fecha_nac = fecha_nac
    def set_sexo(self, sexo: str) -> None:
        """
        Establece el sexo del paciente.
        params:
            - sexo: El nuevo sexo del paciente.
        """
        self._sexo = sexo
    def set_t_sangre(self, t_sangre: str) -> None:
        """
        Establece el tipo de sangre del paciente.
        params:
            - t_sangre: El nuevo tipo de sangre del paciente.
        """
        self._t_sangre = t_sangre

    @abstractmethod
    def __repr__(self):
        """
        Método abstracto que crea una representación en cadena de un objeto.  
        returns:
            Un str con los datos del paciente. 
        """
        pass
    

