from abc import ABC, abstractmethod
from datetime import *

class Vehiculo(ABC):

    def __init__(self, velocidad):
        self.velocidad = velocidad
        self.registro_viajes = []
        self.estado = True #True = Desocupado False = Ocupado

    @abstractmethod
    def realizar_transporte(self,distancia: int, nivel_trafico: int, tiempo_hablacion_donante : time):
        tiempo = (self.velocidad/distancia) + nivel_trafico #se toma el tiempo como horas
        dt = datetime.combine(datetime.today(), tiempo_hablacion_donante)
        nueva_dt = dt + timedelta(hours = tiempo) #agrego el tiempo de transporte al de la hablacion del donante
        tiempo_final = nueva_dt.time()

        return tiempo_final
    