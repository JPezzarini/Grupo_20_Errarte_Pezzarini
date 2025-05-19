from pacientes import Paciente
from datetime import *
from organo import Organo
from centro_de_salud import Centro_Salud

class Receptor(Paciente):


    def __init__(self, nombre: str, dni: int, fecha_nac: str, sexo: str, tel: str, t_sangre: str, centro_salud: Centro_Salud, organo_r : Organo, dt_espera: datetime, patologia: str, estado: str ):
        super().__init__(nombre, dni, fecha_nac, sexo, tel, t_sangre, centro_salud)
        self.organo_r = organo_r
        self.dt_espera = dt_espera
        self.patologia = patologia
        self.estado = estado
        self.prioridad = self.calcular_prioridad()
        

    def calcular_prioridad(self):
        #La prioridad es un numero del 1 al 10. Esta funcion la calcula
        if self.estado == "Inestable":
            self.prioridad = 10
            return self.prioridad

        else:
            fecha_nacimiento_date = self._fecha_nac.date()  ##Convierto la fecha datetime a date
            edad = (date.today() - fecha_nacimiento_date)
            edad = edad.days // 365
            if (edad < 18):
                self.prioridad = 8
            if (edad >=18 and edad<40):
                self.prioridad = 6
            if (edad >= 40 and edad < 65):
                self.prioridad = 4
            if (edad >= 65):
                self.prioridad = 2
        return self.prioridad
            
    def __repr__(self):
        return f"Nombre: {self._nombre}, DNI: {self._dni}, Fecha de nacimiento: {self._fecha_nac}, Sexo: {self._sexo}, Teléfono: {self.tel}, Sangre: {self._t_sangre}, Centro: {self.centro_salud.nombre}, Organo: {self.organo_r._tipo.name}, Ingreso a la lista de espera: {self.dt_espera}, Patología: {self.patologia}, Estado: {self.estado}"