from vehiculo import Vehiculo
from datetime import *

class Ambulancia(Vehiculo):

    def __init__(self, velocidad):
        super().__init__(velocidad)


    def realizar_transporte(self,distancia: int, nivel_trafico: int, fecha_hablacion_donante : datetime, viaje:str):
        tiempo = (self.velocidad/distancia) + nivel_trafico #se toma el tiempo como horas
        tiempo_final = fecha_hablacion_donante + timedelta(hours = tiempo) #sumo el tiempo de transporte a la fecha de hablacion del organo
        self.registro_viajes.append(viaje)
        if datetime.today() < tiempo_final:
            self.estado = False
        return tiempo_final