from vehiculos.vehiculo import Vehiculo
from datetime import *


class Helicoptero(Vehiculo):

    def __init__(self, velocidad):
        super().__init__(velocidad)


    def realizar_transporte(self,distancia: int, nivel_trafico: int, fecha_ablacion_donante : datetime, viaje:str):
        tiempo = nivel_trafico + (distancia.__floordiv__(self.velocidad)) #se toma el tiempo como horas
        tiempo_final = fecha_ablacion_donante + timedelta(hours = tiempo) #sumo el tiempo de transporte a la fecha de ablacion del organo
        self.registro_viajes.append(viaje)
        if datetime.today() < tiempo_final:
            self.estado = False
        return tiempo_final