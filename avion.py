from vehiculo import Vehiculo

class Avion(Vehiculo):

    def __init__(self, velocidad):
        super().__init__(velocidad)


    def realizar_transporte(self,distancia: int, nivel_trafico: int):
        pass