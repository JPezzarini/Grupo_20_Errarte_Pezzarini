from personas.pacientes import Paciente
from datetime import *
from centro_de_salud import Centro_Salud
from organo import *


class Donante(Paciente):
    """
    Esta clase representa a un donante. Hereda los atributos de la clase Paciente.
    """

    def __init__(self, nombre: str, dni: int, fecha_nac: datetime, sexo: str, tel: str, t_sangre: str, centro_salud: Centro_Salud, dt_fallecimiento: str, lista_organos: list):
        """
        Inicializa un Donante.
        
        Atributos:
            - nombre (str): El nombre del donante.
            - dni (int): El DNI del donante.
            - fecha_nac (datetime): La fecha de nacimiento del donante.
            - sexo (str): El sexo del donante (M/F).
            - tel (str): El número de teléfono del donante.
            - t_sangre (str): El tipo de sangre del donante.
            - centro_salud (Centro_Salud): El centro de salud al que está asociado el donante.
            - dt_fallecimiento (str): La fecha de fallecimiento del donante.
            - lista_organos (list): La lista de órganos del donante.

        returns:
            None.
        """

        super().__init__(nombre, dni, fecha_nac, sexo, tel, t_sangre, centro_salud)
        self.dt_fallecimiento = dt_fallecimiento
        self.lista_organos = lista_organos
        

    def __repr__(self):
        """
        Retorna todos los atributos del donante.
        """

        return f"Nombre: {self._nombre}, DNI: {self._dni}, Fecha de nacimiento: {self._fecha_nac}, Sexo: {self._sexo}, Teléfono: {self.tel}, Sangre: {self._t_sangre}, Centro: {self.centro_salud.nombre}, Organos: {[organo._tipo.name for organo in self.lista_organos]}, Fallecimiento: {self.dt_fallecimiento}"