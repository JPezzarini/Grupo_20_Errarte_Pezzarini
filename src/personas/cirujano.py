from otros.organo import *
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
    """
    Esta clase representa a un cirujano capaz de realizar operaciones a receptores.
    """

    def __init__(self, especialidad, nombre: str): 
        """
        Inicializa un Cirujano.
        
        params:
            - especialidad(Especialidad): La especialidad del cirujano.
              Puede inicializarse con un int o con un valor del enum Especialidad
            - fecha_ultima_operacion (datetime): La fecha en la que el cirujano realizó su última operación
            - estado (bool): El estado del cirujano. True si está desocupado, False si está ocupado
            - nombre (str): El nombre del cirujano.

        returns:
            None.
        """

        if isinstance(especialidad, int):
            self.especialidad = Especialidad(especialidad) #Convierte int a enum
        elif isinstance(especialidad, Especialidad):
            self.especialidad = especialidad #Asigna directamente enum
        self.fecha_ultima_operacion = None
        self.estado = True
        self.nombre = nombre

    def determinar_disponibilidad(self, fecha: datetime) -> None:
        """
        Determina la disponibilidad del cirujano basado en la fecha de la última operación.
        Si pasaron más de 24 horas, el cirujano queda disponible.

        params:
            - fecha (datetime): Un objeto datetime que representa la fecha actual.
        
        returns:
            None.
        """
        if self.fecha_ultima_operacion != None:
            diferencia = (fecha - self.fecha_ultima_operacion).days
            if diferencia >= 1:
                self.estado = True
        else:
            self.estado = True


    def __eq__(self, organo: Organo) -> bool:
        """
        Compara la especialidad del cirujano con el tipo de órgano que se pasó como parámetro.

        params:
            - organo (Organo): El órgano que se desea comparar.

        returns:
            True si la especialidad coincide con el tipo de órgano y False si no.
        """

        if isinstance(organo, Organo):
            if self.especialidad.value == 1 and organo.get_tipo().value == 1: #Cardiovascular y corazón
                return True
            if self.especialidad.value == 2 and organo.get_tipo().value == 2: #Pulmonar y pulmón
                return True
            if self.especialidad.value == 3 and (organo.get_tipo().value == 3 or organo.get_tipo().value == 4): #Plástico y piel o córnea
                return True
            if self.especialidad.value == 4 and organo.get_tipo().value == 5: #Traumatólogo y hueso
                return True
            if self.especialidad.value == 5 and (organo.get_tipo().value == 6 or organo.get_tipo().value == 7 or organo.get_tipo().value == 8 or organo.get_tipo().value == 9): #Gastroenterologo e intestino, riñón, hígado y páncreas
                return True
        return False
    