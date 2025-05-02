from pacientes import Paciente
from datetime import *

class Donante(Paciente):


    def __init__(self, nombre: str, DNI: int, fecha_nac: datetime, sexo: str, tel: str, t_sangre: str, centro_salud, dt_fallecimiento: datetime, dt_ablacion: datetime, lista_organos: list):
        super().__init__(nombre, DNI, fecha_nac, sexo, tel, t_sangre, centro_salud)
        self.dt_fallecimiento = dt_fallecimiento
        self.dt_ablacion = dt_ablacion
        self.lista_organos = lista_organos
        

    def _nada(self):
        return