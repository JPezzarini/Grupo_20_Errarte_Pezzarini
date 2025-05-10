from organo import *
from enum import Enum
from datetime import *
class Especialidad(Enum):
    general = 0
    cardiovascular = 1
    pulmonar = 2
    plastico = 3
    traumatologo = 4
    gastroenterologo = 5

class Cirujano:

    def __init__(self, especialidad):
        if isinstance(especialidad, int):
            self.especialidad = Especialidad(especialidad) #Convierte int a enum
        elif isinstance(especialidad, Especialidad):
            self.especialidad = especialidad #Asigna directamente enum
        self.fecha_ultima_operacion = None
        self.estado = True #True = Desocupado False = Ocupado

    def determinar_disponibilidad(self, fecha: datetime):
        if self.fecha_ultima_operacion != None:
            diferencia = (fecha - self.fecha_ultima_operacion).days
            if diferencia <=1:
                self.estado = True
        else:
            self.estado = True

    def __eq__(self, organo: Organo):
        if isinstance(organo, Organo):
            
            if self.especialidad.value==1 and organo._tipo.value == 1: #Cardiovascular y corazón
                return True
            if self.especialidad.value==2 and organo._tipo.value == 2: #Pulmonar y pulmón
                return True
            if self.especialidad.value == 3 and (organo._tipo.value == 3 or organo._tipo.value == 4): #Plástico y piel o córnea
                return True
            if self.especialidad.value==4 and organo._tipo.value == 5: #Traumatólogo y hueso
                return True
            if self.especialidad.value==5 and (organo._tipo.value == 6 or organo._tipo.value == 7 or organo._tipo.value == 8 or organo._tipo.value == 9): #Gastroenterologo e intestino, riñón, hígado y páncreas
                return True
        return False
    