from abc import ABC, abstractmethod
from datetime import *

class Vehiculo(ABC):

    def __init__(self, velocidad):
        self.velocidad = velocidad
        self.registro_viajes = []
        self.estado = True #True = Desocupado False = Ocupado

    @abstractmethod
    def realizar_transporte(self,distancia: int, nivel_trafico: int, fecha_hablacion_donante : datetime, viaje:str):
        tiempo = (self.velocidad/distancia) + nivel_trafico #se toma el tiempo como horas
        tiempo_final = fecha_hablacion_donante + timedelta(hour = tiempo) #sumo el tiempo de transporte a la fecha de hablacion del organo
        self.registro_viajes.append(viaje)
        return tiempo_final
    