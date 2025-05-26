from personas.pacientes import Paciente
from datetime import *
from centro_de_salud import Centro_Salud
from organo import *
class Donante(Paciente):


    def __init__(self, nombre: str, dni: int, fecha_nac: datetime, sexo: str, tel: str, t_sangre: str, centro_salud: Centro_Salud, dt_fallecimiento: str, lista_organos: list):
        super().__init__(nombre, dni, fecha_nac, sexo, tel, t_sangre, centro_salud)
        self.dt_fallecimiento = dt_fallecimiento
        self.lista_organos = lista_organos
        

    def __repr__(self):
        return f"Nombre: {self._nombre}, DNI: {self._dni}, Fecha de nacimiento: {self._fecha_nac}, Sexo: {self._sexo}, Teléfono: {self.tel}, Sangre: {self._t_sangre}, Centro: {self.centro_salud.nombre}, Organos: {[organo._tipo.name for organo in self.lista_organos]}, Fallecimiento: {self.dt_fallecimiento}"