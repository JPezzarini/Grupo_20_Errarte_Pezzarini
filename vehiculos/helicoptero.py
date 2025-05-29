from vehiculos.vehiculo import Vehiculo
from datetime import *


class Helicoptero(Vehiculo):
    """
    Esta clase representa a una helicóptero. Hereda atributos de la clase Vehiculo.
    """
    def __init__(self, velocidad):
        """
        Inicializa un objeto helicóptero

        Atributos:
            - velocidad (int): La velocidad del vehículo.
            - registro_viajes (list): Lista de viajes realizados por el vehículo.
            - estado (bool): Estado del vehículo. True indica que está desocupado y False que está ocupado.
        """
        super().__init__(velocidad)


    def realizar_transporte(self,distancia: int, nivel_trafico: int, fecha_ablacion_donante : datetime, viaje:str) -> datetime:
        """
        Método abstracto para realizar el transporte de órganos.
        params:
            - distancia (int): La distancia a recorrer en kilómetros.
            - nivel_trafico (int): El nivel de tráfico.
            - fecha_ablacion_donante (datetime): La fecha de ablación del órgano del donante.
            - viaje (str): Inicio y destino del viaje.
        returns:
            Un objeto datetime que representa la suma de la fecha de ablación del órgano y el tiempo de transporte
        """
        tiempo = nivel_trafico + (distancia.__floordiv__(self.velocidad))
        tiempo_final = fecha_ablacion_donante + timedelta(hours = tiempo)
        self.registro_viajes.append(viaje)
        if datetime.today() < tiempo_final:
            self.estado = False
        return tiempo_final