from abc import ABC, abstractmethod

class Vehiculo(ABC):

    def __init__(self, velocidad):
        self.velocidad = velocidad
        self.registro_viajes = []
        self.estado = True #True = Desocupado False = Ocupado

    @abstractmethod
    def realizar_transporte(self):
        pass
        #Falta terminar