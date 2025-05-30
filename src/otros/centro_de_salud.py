from vehiculos.avion import Avion
from vehiculos.helicoptero import Helicoptero
from vehiculos.ambulancia import Ambulancia
from random import *
from otros.organo import *
from personas.cirujano import *
from datetime import *


class Centro_Salud:
    """
    Esta clase representa un centro de salud que gestiona cirujanos y vehículos para realizar trasplantes.
    """

    def __init__(self, nombre: str, partido: str, provincia: str, tel: str, cirujanos: list[Cirujano], vehiculos: list):
        """
        Inicializa un centro de salud.
        Atributos:
            - nombre (str): El nombre del centro de salud.
            - partido (str): El partido donde se ubica el centro de salud.
            - provincia (str): La provincia donde se ubica el centro de salud.
            - telefono (str): El número de teléfono del centro de salud.
            - lista_cirujanos (list): Lista de cirujanos disponibles en el centro de salud.
            - lista_vehiculos (list): Lista de vehículos disponibles para el transporte.
        """
        self.nombre = nombre
        self.partido = partido
        self.provincia = provincia
        self.telefono = tel
        self.lista_cirujanos = cirujanos
        self.lista_vehiculos = vehiculos



    def asignar_vehiculo(self, centro_receptor, viaje, fecha_ablacion_donante) -> bool:
        """
        Asigna un vehículo adecuado para el transporte de órganos según la ubicación del centro receptor. 
        Llama a la función ordenar_vehículo_velocidad.

        params:
            - centro_receptor: El centro de salud del paciente receptor.
            - viaje: Información sobre el viaje que se va a realizar.
            - fecha_ablacion_donante: La fecha de ablación del órgano del donante.

        returns:
            Retorna un booleano. True si se logró asignar un vehículo correctamente, False en caso contrario.
        """        

        self.ordenar_vehiculo_velocidad()
        if (self.provincia == centro_receptor.provincia and self.partido == centro_receptor.partido):
            for i in range (len(self.lista_vehiculos)):
                if isinstance(self.lista_vehiculos[i], Ambulancia):
                    if (self.lista_vehiculos[i].estado):
                        distancia = randint(1,25) #en km
                        nivel_trafico = uniform(0,2)
                        self.lista_vehiculos[i].realizar_transporte(distancia, nivel_trafico, fecha_ablacion_donante, viaje)
                        return True
        if (self.provincia == centro_receptor.provincia and self.partido != centro_receptor.partido):
            for i in range (len(self.lista_vehiculos)):
                if isinstance(self.lista_vehiculos[i], Helicoptero):
                    if (self.lista_vehiculos[i].estado):
                        distancia = randint(25,100) #en km
                        nivel_trafico = 0
                        self.lista_vehiculos[i].realizar_transporte(distancia, nivel_trafico, fecha_ablacion_donante, viaje)
                        return True
        if (self.provincia != centro_receptor.provincia):
            for i in range (len(self.lista_vehiculos)):
                if isinstance(self.lista_vehiculos[i], Avion):
                    if (self.lista_vehiculos[i].estado):
                        distancia = randint(100,3000) #en km
                        nivel_trafico = 0
                        self.lista_vehiculos[i].realizar_transporte(distancia, nivel_trafico, fecha_ablacion_donante, viaje)
                        return True
        
        print("No se pudo asignar un vehículo adecuado en este momento")
        return False
    
    
    def ordenar_vehiculo_velocidad(self) -> None:
        """
        Ordena la lista de vehículos por velocidad en orden descendente.
        """ 
        for i in range (len(self.lista_vehiculos)):
            for k in range (0, len(self.lista_vehiculos)-1-i):
                if(self.lista_vehiculos[k+1].velocidad > self.lista_vehiculos[k].velocidad):
                    a = self.lista_vehiculos[k]
                    self.lista_vehiculos[k] = self.lista_vehiculos[k+1]
                    self.lista_vehiculos[k+1] = a
    

    def realizar_transplante(self, cirujano: Cirujano, receptor, organo: Organo) -> bool:
        """
        Realiza el transplante del órgano del donante al receptor.
        El transplante es realizado por el cirujano asignado previamente.

        params:
            - cirujano: El cirujano que realizará el trasplante.
            - receptor (Receptor): El receptor del órgano trasplantado.
            - organo: El órgano que se va a trasplantar.

        returns:
            Retorna un booleano. True si la operación fue exitosa, False en caso contrario.
        """

        cirujano.estado = False
        if (cirujano == organo):
            probabilidad  = randint(1, 10)
            if (probabilidad >=3 ):
                print("La operación ha sido un éxito")
                return True
            else:
                print("La cirugía ha fallado")
                receptor.estado = "inestable"
                receptor.calcular_prioridad()
                return False

        else:
            probabilidad  = randint(1, 10)
            if (probabilidad >=5 ):
                print("La operación ha sido un éxito")
                return True

            else:
                print("La cirujía ha fallado")
                receptor.estado = "inestable"
                receptor.calcular_prioridad()
                return False


    def asignar_cirujano(self, receptor, organo: Organo) -> bool:
        """
        Asigna un cirujano disponible para realizar un trasplante.
        Llama a la función realizar_transplante.

        params:
            - receptor (Receptor): El receptor del órgano trasplantado.
            - organo: El órgano que se va a trasplantar.

        returns:
            Retorna el valor de la función realizar_transplante (bool).
        """

        fecha_transplante = datetime.today()
        for i in range (len(self.lista_cirujanos)):
                self.lista_cirujanos[i].determinar_disponibilidad(fecha_transplante)
                if (self.lista_cirujanos[i] == organo and self.lista_cirujanos[i].estado == True):
                    self.lista_cirujanos[i].fecha_ultima_operacion = fecha_transplante
                    self.lista_cirujanos[i].estado = False
                    return self.realizar_transplante(self.lista_cirujanos[i], receptor, organo) #si encuentra un cirujano que coincida y esté disponible sale de la función
                    
        #Si no encuentra un especialista disponible, asigna al primer cirujano disponible, no importa especialidad        
        for i in range (len(self.lista_cirujanos)):
            self.lista_cirujanos[i].determinar_disponibilidad(fecha_transplante)
            if (self.lista_cirujanos[i].estado):
                self.lista_cirujanos[i].fecha_ultima_operacion = fecha_transplante
                return self.realizar_transplante(self.lista_cirujanos[i], receptor, organo)
                

    def chequear_disponibilidad_cirujano(self) -> bool:
        """
        Verifica si hay cirujanos disponibles en el centro de salud.

        returns:
            Retorna un booleano. True si hay al menos un cirujano disponible, False en caso contrario.
        """

        cont = 0
        for i in range (len(self.lista_cirujanos)):
            if self.lista_cirujanos[i].estado == True:
                cont += 1
        if cont > 0:
            return True
        else:
            return False