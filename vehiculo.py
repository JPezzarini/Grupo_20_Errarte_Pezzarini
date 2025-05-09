from abc import ABC, abstractmethod
from datetime import *

class Vehiculo(ABC):

    def __init__(self, velocidad):
        self.velocidad = velocidad
        self.registro_viajes = []
        self.estado = True #True = Desocupado False = Ocupado

    @abstractmethod
    def realizar_transporte(self,distancia: int, nivel_trafico: int, fecha_hablacion_donante : datetime, viaje:str):
        pass
    