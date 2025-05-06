from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from datetime import *
from donantes import Donante
from receptores import Receptor
from vehiculo import Vehiculo
import random
if TYPE_CHECKING:
    from pacientes import Paciente
    from organo import Organo
    from centro_de_salud import Centro_Salud
    from ambulancia import Ambulancia
    from avion import Avion
    from helicoptero import Helicoptero

class Sistema():


    def __init__(self, centros_salud):
        self.lista_receptores = []
        self.lista_donantes = []
        self.lista_centros = centros_salud



    def recibir_paciente(self, paciente: Paciente):
        if isinstance(paciente, Donante):
            self.recibir_donante(paciente)
        else:
            self.recibir_receptor(paciente)


    def recibir_donante(self, donante):
        self.lista_donantes.append(donante)

    def recibir_receptor(self, receptor):
        self.lista_receptores.append(receptor)
    

    def elegir_receptor(self, receptores: list):
        #La lista de receptores tiene todos los receptores compatibles que necesiten el órgano especificado
        #Esta lista fue hecha en la funcion buscar_match
        
        for i in range(len(receptores)):
            for k in range (0,len(receptores)-1-i):
                if(receptores[k+1].prioridad > receptores[k].prioridad):
                    a = receptores[k]
                    receptores[k] = receptores[k+1]
                    receptores[k+1] = a
        receptor_match = self.elegir_receptor_prioridad(receptores)
        return receptor_match # retorna el receptor de mayor prioridad


    def elegir_receptor_prioridad(self, receptores: list):
        for i in range(len(receptores)):
            for k in range (0,len(receptores)-1-i):
                if(receptores[k+1].dt_espera > receptores[k].dt_espera and receptores[k+1].prioridad == receptores[k].prioridad):
                    a = receptores[k]
                    receptores[k] = receptores[k+1]
                    receptores[k+1] = a
        return receptores[0]



    def buscar_match(self,donante: Donante,organo: Organo): # el organo es el primero de la lista del donante
        receptores = []
        for i in range(len(self.lista_receptores)):
            if(self.lista_receptores[i].organo_r._tipo == organo._tipo and self.lista_receptores[i]._t_sangre == donante._t_sangre):
                receptores.append(self.lista_receptores[i])
        receptor_match = self.elegir_receptor(receptores)
        hoy = date.today()
        donante.lista_organos[0].dt_hablacion = datetime.combine(hoy,time(random.randint(0,23),random.randint(0,59),random.randint(0,59))) # creo una fecha y tiempo de ablacion random
        donante.centro_salud.asignar_vehiculo(receptor_match.centro_salud)

