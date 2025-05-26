from abc import ABC, abstractmethod
from datetime import *

class Vehiculo(ABC):
    """
    Esta clase abstracta representa un vehículo utilizado para realizar el transporte de órganos.
    """
    def __init__(self, velocidad):
        """
        Inicializa un vehículo
        Atributos:
            - velocidad (int): La velocidad del vehículo.
            - registro_viajes (list): Lista de viajes realizados por el vehículo.
            - estado (bool): Estado del vehículo. True indica que está desocupado y False que está ocupado.
        """
        self.velocidad = velocidad
        self.registro_viajes = []
        self.estado = True

    @abstractmethod
    def realizar_transporte(self,distancia: int, nivel_trafico: int, fecha_ablacion_donante : datetime, viaje:str) -> datetime:
        """
        Método abstracto para realizar el transporte de órganos.
        params:
            distancia (int): La distancia a recorrer en kilómetros.
            nivel_trafico (int): El nivel de tráfico.
            fecha_ablacion_donante (datetime): La fecha de ablación del órgano del donante.
            viaje (str): Inicio y destino del viaje.
        returns:
            Un objeto datetime que representa la suma de la fecha de ablación del órgano y el tiempo de transporte
        """
        pass
    