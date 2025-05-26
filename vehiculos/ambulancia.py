from vehiculos.vehiculo import Vehiculo
from datetime import *

class Ambulancia(Vehiculo):
    """
    Esta clase representa a una ambulancia. Hereda atributos de la clase Vehiculo.
    Aclaración: la función realizar_transporte ya fue comentada en la clase Vehiculo.
    """

    def __init__(self, velocidad):
        super().__init__(velocidad)


    def realizar_transporte(self,distancia: int, nivel_trafico: int, fecha_ablacion_donante : datetime, viaje:str) -> datetime:
        tiempo = nivel_trafico + (distancia.__floordiv__(self.velocidad))
        tiempo_final = fecha_ablacion_donante + timedelta(hours = tiempo)
        self.registro_viajes.append(viaje)
        if datetime.today() < tiempo_final:
            self.estado = False
        return tiempo_final