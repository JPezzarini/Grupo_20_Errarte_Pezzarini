from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from datetime import *
if TYPE_CHECKING:
    from pacientes import Paciente
    from donantes import Donante
    from receptores import Receptor
    from organo import Organo

class Sistema():


    def __init__(self, centros_salud):
        self.lista_receptores = []
        self.lista_donantes = []
        self.lista_centros = centros_salud



    def recibir_paciente(self, paciente: Donante or Receptor):
        if type(paciente) is Donante:
            self.recibir_donante(paciente)
        else:
            self.recibir_receptor(paciente)


    def recibir_donante(self, donante):
        self.lista_donantes.append(donante)

    def recibir_receptor(self, receptor):
        self.lista_receptores.append(receptor)
    

    def elegir_receptor(self, receptores: list):
        """La lista de receptores tiene todos los receptores compatibles que necesiten el órgano especificado
            Esta lista fue hecha en la funcion buscar match
        """
    def elegir_receptor_prioridad(self, receptores: list):
        """
        bubble sort
        """
