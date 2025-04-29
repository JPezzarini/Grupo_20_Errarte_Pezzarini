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



    def recibir_paciente(self, paciente: Paciente):
        if type(paciente) is Donante:
            self.recibir_donante(paciente)
        else:
            self.recibir_receptor(paciente)


    def recibir_donante(self, donante):
        self.lista_donantes.append(donante)

    def recibir_receptor(self, receptor):
        self.lista_receptores.append(receptor)
    

    def elegir_receptor_prioridad(self, receptores: list):
        """
        bubble sort
        """
        for i in range(len(receptores)):
            for k in range (0,len(receptores)-1-i):
                if(receptores[k+1].dt_espera > receptores[k].dt_espera and receptores[k+1].prioridad == receptores[k].prioridad):
                    a = receptores[k]
                    receptores[k] = receptores[k+1]
                    receptores[k+1] = a


    def elegir_receptor(self, receptores: list):
        """La lista de receptores tiene todos los receptores compatibles que necesiten el órgano especificado
            Esta lista fue hecha en la funcion buscar match
        """
        for i in range(len(receptores)):
            for k in range (0,len(receptores)-1-i):
                if(receptores[k+1].prioridad > receptores[k].prioridad):
                    a = receptores[k]
                    receptores[k] = receptores[k+1]
                    receptores[k+1] = a
        self.elegir_receptor_prioridad(receptores)


    def buscar_match(self,donante: Donante,organo: Organo):
        receptores = []
        for i in range(len(self.lista_receptores)):
            if(self.lista_receptores[i].organo_r.__tipo == organo.__tipo and self.lista_receptores[i]._t_sangre == donante._t_sangre):
                receptores.append(self.lista_receptores[i])
        self.elegir_receptor(receptores)
        

