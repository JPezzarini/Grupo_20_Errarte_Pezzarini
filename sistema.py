from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from datetime import *
from donantes import Donante
from receptores import Receptor
from vehiculo import Vehiculo
import random
from organo import *
if TYPE_CHECKING:
    from pacientes import Paciente
    from centro_de_salud import Centro_Salud
    from ambulancia import Ambulancia
    from avion import Avion
    from helicoptero import Helicoptero
    from cirujano import Cirujano

class Sistema():


    def __init__(self, centros_salud: list, lista_receptores: list, lista_donantes: list):
        self.lista_receptores = lista_receptores
        self.lista_donantes = lista_donantes
        self.lista_centros = centros_salud



    def recibir_paciente(self, paciente: Paciente):
        # esta funcon agrega un paciente a sistema, lo agreaga a la lista de donantes o receptores dependiendo lo que se ingrese
        #llama a las funciones recibir_donante y recibir_receptor respectivamente

        if isinstance(paciente, Donante):
            self.recibir_donante(paciente)
        else:
            self.recibir_receptor(paciente)


    def recibir_donante(self, donante: Donante):
        #agrega al donante al sistema y busca match con los receptores del mismo
        #los while sirven para que no se vayan de rango la slistas si retiramos un elemento de ellas

        self.lista_donantes.append(donante)
        i=0
        while i < (len(donante.lista_organos)):
            k = i
            self.buscar_match_donante(donante,donante.lista_organos[i],k)
            i+=1

    def recibir_receptor(self, receptor: Receptor):
        #agrega al receptor al sistema y busca match con los donantes del mismo

        self.lista_receptores.append(receptor)
        self.buscar_match_receptor(receptor)
    

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
        #se ordena la lista de receptores compatibles en, caso de que tengan la misma prioridad, por antiguedad en el sistema

        for i in range(len(receptores)):
            for k in range (0,len(receptores)-1-i):
                if(receptores[k+1].dt_espera > receptores[k].dt_espera and receptores[k+1].prioridad == receptores[k].prioridad):
                    a = receptores[k]
                    receptores[k] = receptores[k+1]
                    receptores[k+1] = a
        return receptores[0]
    


    def buscar_match_donante(self,donante: Donante,organo: Organo, k):
        #busca receptores compatibles segun el donante pasado como parametro, armando una lista de ellos
        #pasa la lista a las funciones de ordenamiento, que devuelven el receptor final para la operacion 

        receptores = []
        for i in range(len(self.lista_receptores)):
            if(self.lista_receptores[i].organo_r._tipo == organo._tipo and self.lista_receptores[i]._t_sangre == donante._t_sangre):
                receptores.append(self.lista_receptores[i])
        
        if(len(receptores) == 0):
            print("No se encontraron receptores que cualifiquen") #printea si no encuentra match
            return
        
        receptor_match = self.elegir_receptor(receptores) #receptor de mayor prioridad
        
        if (receptor_match.centro_salud.chequear_disponibilidad_cirujano()):
            
            hoy = date.today()
            donante.lista_organos[k].dt_hablacion = datetime.combine(hoy,time(random.randint(0,23),random.randint(0,59),random.randint(0,59))) # creo una fecha y tiempo de ablacion random
            fecha_hablacion = donante.lista_organos[k].dt_hablacion #guarda la fecha en una variable para pasarla entre funciones
            viaje = f"{donante.centro_salud.nombre}-{receptor_match.centro_salud.nombre}" #guarda el viaje para pasarselo al vehiculo
            donante.centro_salud.asignar_vehiculo(receptor_match.centro_salud,viaje,fecha_hablacion)
            
            if (receptor_match.centro_salud.asignar_cirujano(receptor_match, donante.lista_organos[k])): #si sale bien se retira el organo y se retira el receptor de la lista
                self.lista_receptores.remove(receptor_match)
                donante.lista_organos.remove(organo)
            
            else: #si sale mal se pierde el organo y el receptor pasa a estar inestable
                donante.lista_organos.remove(organo)
                receptor_match.estado = "Inestable"
        
        else:
            print("No hay cirujanos disponibles")
    

    def buscar_match_receptor(self, receptor: Receptor):
        #busca al primer donante compatible segun el receptor pasado como parametro
        #los while sirven para que no se vayan de rango la slistas si retiramos un elemento de ellas

        i = 0
        while i < (len(self.lista_donantes)):
            k=0
            while k < (len(self.lista_donantes[i].lista_organos)):
                if(receptor.organo_r._tipo == self.lista_donantes[i].lista_organos[k]._tipo and receptor._t_sangre == self.lista_donantes[i]._t_sangre):
                    if (receptor.centro_salud.chequear_disponibilidad_cirujano()):
                        hoy = date.today()
                        self.lista_donantes[i].lista_organos[k].dt_hablacion = datetime.combine(hoy,time(random.randint(0,23),random.randint(0,59),random.randint(0,59))) # creo una fecha y tiempo de ablacion random
                        fecha_hablacion = self.lista_donantes[i].lista_organos[k].dt_hablacion #guardo la fecha en una variable para pasarla entre funciones
                        viaje = f"{self.lista_donantes[i].centro_salud.nombre}-{receptor.centro_salud.nombre}" #me guardo el viaje para pasarselo al vehiculo 
                        if(self.lista_donantes[i].centro_salud.asignar_vehiculo(receptor.centro_salud,viaje,fecha_hablacion)):

                            if (receptor.centro_salud.asignar_cirujano(receptor, self.lista_donantes[i].lista_organos[k])): #si sale bien se retira el organo y se retira el receptor de la lista
                                self.lista_receptores.remove(receptor)

                            else: #si sale mal se pierde el organo y el receptor pasa a estar inestable
                                receptor.estado = "Inestable"

                            self.lista_donantes[i].lista_organos.pop(k)
                            if (self.lista_donantes[i].lista_organos): #Si el donante ya no tiene más organos se retira al donante de la lista
                                self.lista_donantes.pop(i)
                    else:
                        print("No hay cirujanos disponibles")
                k+=1
            i+= 1
                
    def crear_paciente(self, centro_salud: Centro_Salud):
        #se crea un paciente pasando los parametros a mano, luego llama a las respectivas funciones de buscar_match

        nombre = str(input("Ingrese el nombre del paciente: "))
        try:
            dni = int(input("Ingrese el DNI del paciente: "))
            for i in range(len(self.lista_receptores)):
                if(self.lista_receptores[i]._dni == dni):
                    raise ValueError("Entrada inválida, DNI ya registrado")
            for i in range(len(self.lista_donantes)):
                if(self.lista_donantes[i]._dni == dni):
                    raise ValueError("Entrada inválida, DNI ya registrado")    
        except ValueError as e:
            print(e)
            exit(1)
        fecha_nacimiento = str(input("Ingrese su fecha de nacimiento AAAA/MM/DD: "))
        try:
            sexo = str(input("Ingrese el sexo del paciente, Masculino = M, Femenino = F: ").strip().upper())
            if sexo not in ("M", "F"):
               raise ValueError("Entrada inválida, solo se acepta 'M' o 'F'.")
        except ValueError as e:
            print(e)
            exit(1)
        try:
            telefono = str(input("Ingrese el telefono del paciente: "))
            for i in range(len(self.lista_receptores)):
                if(self.lista_receptores[i].tel == telefono):
                    raise ValueError("Entrada inválida, telefono ya registrado")
            for i in range(len(self.lista_donantes)):
                if(self.lista_donantes[i].tel == telefono):
                    raise ValueError("Entrada inválida, telefono ya registrado")    
        except ValueError as e:
            print(e)
            exit(1)
        try:
            tipo_sangre = str(input("Ingrese su tipo de sangre: "))
            if sexo not in ("A+","A-","B+","B-","O+","O-","AB+","AB-"):
               raise ValueError("Entrada inválida, tipo de sangre no existente")
        except ValueError as e:
            print(e)
            exit(1)
        try:
            tipo_paciente = input("Su paciente es donante o receptor? Donante = D; Receptor = R: ")
            if tipo_paciente not in ("D", "R"):
               raise ValueError("Entrada inválida, tipo de paciente no existente")
        except ValueError as e:
            print(e)
            exit(1)
        if (tipo_paciente == "D"):
            dt_fallecimiento = str(input("ingrese la fecha de fallecimiento AAAA/MM/DD: "))
            lista_organos = []
            cantidad_organos = int(input("ingrese la cantidad de organos: "))
            for i in range (0,cantidad_organos):
                tipo = str(input("ingrese el tipo de organo: "))
                organo_i = Organo(Tipo[tipo])
                lista_organos.append(organo_i)
            paciente = Donante(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud, dt_fallecimiento, lista_organos)
            i=0
            while i < (len(paciente.lista_organos)):
                k = i
                self.buscar_match_donante(paciente, paciente.lista_organos[i],k)
                i+=1

        else:
            tipo = str(input("ingrese el tipo de organo: "))
            organo_r = Organo(Tipo[tipo])
            str_espera = str(input("ingrese la fecha de ingreso al sistema del instituto AAAA/MM/DD: "))
            dt_espera = datetime.strptime(str_espera,"%Y-%m-%d")
            patologia = str(input("ingrese su patologia: "))
            estado = str(input("ingrese su estado: "))
            paciente = Receptor(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud, organo_r, dt_espera, patologia,estado)
            self.buscar_match_receptor(paciente)



    def listar_receptores(self):
        #printea la lista de receptores del sistema

        if self.lista_receptores == False:
            print("No hay receptores en el sistema")
            return
        
        for i in range (len(self.lista_receptores)):
            print(self.lista_receptores[i].__repr__())

    def listar_donantes(self):
        #printea la lista de donantes del sistema

        if self.lista_donantes == False:
            print("No hay donantes en el sistema")
            return
        
        for i in range (len(self.lista_donantes)):
            print(self.lista_donantes[i].__repr__())
                

        
