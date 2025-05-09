from vehiculo import Vehiculo
from datetime import *

class Avion(Vehiculo):

    def __init__(self, velocidad):
        super().__init__(velocidad)


    def realizar_transporte(self,distancia: int, nivel_trafico: int, fecha_hablacion_donante : datetime, viaje:str):
        nivel_trafico = 0
        tiempo = (self.velocidad/distancia) + nivel_trafico #se toma el tiempo como horas
        tiempo_final = fecha_hablacion_donante + timedelta(hour = tiempo) #sumo el tiempo de transporte a la fecha de hablacion del organo
        self.registro_viajes.append(viaje)
        return tiempo_final