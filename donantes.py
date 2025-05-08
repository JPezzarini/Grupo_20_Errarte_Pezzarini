from pacientes import Paciente
from datetime import *
from centro_de_salud import Centro_Salud

class Donante(Paciente):


    def __init__(self, nombre: str, DNI: int, fecha_nac: datetime, sexo: str, tel: str, t_sangre: str, centro_salud: Centro_Salud, dt_fallecimiento: datetime, lista_organos: list):
        super().__init__(nombre, DNI, fecha_nac, sexo, tel, t_sangre, centro_salud)
        self.dt_fallecimiento = dt_fallecimiento
        self.lista_organos = lista_organos
        

    def __nada(self):
        return