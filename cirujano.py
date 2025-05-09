from organo import Organo
from enum import Enum

class Especialidad(Enum):
    general = 0
    cardiovascular = 1
    pulmonar = 2
    plastico = 3
    traumatologo = 4
    gastroenterologo = 5

class Cirujano:

    def __init__(self, especialidad):
        self.especialidad = especialidad
        self.estado = True #True = Desocupado False = Ocupado

          
    def __eq__(self, organo):
        if self.especialidad.value==1 and organo._tipo.value == 1:
            return True
        if self.especialidad.value==2 and organo._tipo.value == 2:
            return True
        if self.especialidad.value == 3 and (organo._tipo.value == 3 or organo._tipo.value == 4):
            return True
        if self.especialidad.value==4 and organo._tipo.value == 5:
            return True
        if self.especialidad.value==1 and (organo._tipo.value == 6 or organo._tipo.value == 7 or organo._tipo.value == 8 or organo._tipo.value == 9):
            return True
        return False
    

