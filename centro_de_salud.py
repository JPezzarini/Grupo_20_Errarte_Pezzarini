from avion import Avion
from helicoptero import Helicoptero
from ambulancia import Ambulancia
from random import *
from organo import *
from cirujano import *
from datetime import *


class Centro_Salud:


    def __init__(self, nombre: str, partido: str, provincia: str, tel: str, cirujanos: list, vehiculos: list):

        self.nombre = nombre
        self.partido = partido
        self.provincia = provincia
        self.telefono = tel
        self.lista_cirujanos = cirujanos
        self.lista_vehiculos = vehiculos



    def asignar_vehiculo(self, centro_receptor, viaje, fecha_hablacion_donante): #falta determinar nivel de trafico y distancia de viaje
        self.ordenar_vehiculo_velocidad()
        if (self.provincia == centro_receptor.provincia and self.partido == centro_receptor.partido):
            for i in range (len(self.lista_vehiculos)):
                if isinstance(self.lista_vehiculos[i], Ambulancia):
                    if (self.lista_vehiculos[i].estado):
                        distancia = randint(1,25) #en km
                        nivel_trafico = uniform(0,2)
                        self.lista_vehiculos[i].realizar_transporte(distancia, nivel_trafico, fecha_hablacion_donante, viaje)
                        return True
        if (self.provincia == centro_receptor.provincia and self.partido != centro_receptor.partido):
            for i in range (len(self.lista_vehiculos)):
                if isinstance(self.lista_vehiculos[i], Helicoptero):
                    if (self.lista_vehiculos[i].estado):
                        distancia = randint(25,100) #en km
                        nivel_trafico = 0
                        self.lista_vehiculos[i].realizar_transporte(distancia, nivel_trafico, fecha_hablacion_donante, viaje)
                        return True
        if (self.provincia != centro_receptor.provincia):
            for i in range (len(self.lista_vehiculos)):
                if isinstance(self.lista_vehiculos[i], Avion):
                    if (self.lista_vehiculos[i].estado):
                        distancia = randint(100,3000) #en km
                        nivel_trafico = 0
                        self.lista_vehiculos[i].realizar_transporte(distancia, nivel_trafico, fecha_hablacion_donante, viaje)
                        return True
        
        print("No se pudo asignar un vehículo adecuado en este momento") #Printea solo si no encontro un vehiculo 
        return False
    
    def ordenar_vehiculo_velocidad(self):
        for i in range (len(self.lista_vehiculos)):
            for k in range (0, len(self.lista_vehiculos)-1-i):
                if(self.lista_vehiculos[k+1].velocidad > self.lista_vehiculos[k].velocidad):
                    a = self.lista_vehiculos[k]
                    self.lista_vehiculos[k] = self.lista_vehiculos[k+1]
                    self.lista_vehiculos[k+1] = a
    
    def realizar_transplante(self, cirujano: Cirujano, receptor, organo: Organo): #Si importo Receptor da un error de circular import
        cirujano.estado = False
        if (cirujano == organo):
            probabilidad  = randint(1, 10)
            if (probabilidad >=3 ):
                print("La operación ha sido un éxito")
                return True
            else:
                print("La cirugía ha fallado")
                receptor.estado = "Inestable"
                receptor.calcular_prioridad()

        else:
            probabilidad  = randint(1, 10)
            if (probabilidad >=5 ):
                print("La operación ha sido un éxito")
                return True

            else:
                print("La cirujía ha fallado")
                receptor.estado = "Inestable"
                receptor.calcular_prioridad()


    def asignar_cirujano(self, receptor, organo: Organo):
        fecha_transplante = datetime.today()
        for i in range (len(self.lista_cirujanos)):
                self.lista_cirujanos[i].determinar_disponibilidad(fecha_transplante)
                if (self.lista_cirujanos[i] == organo and self.lista_cirujanos[i].estado == True):
                    self.lista_cirujanos[i].fecha_ultima_operacion = fecha_transplante
                    self.lista_cirujanos[i].estado = False
                    return self.realizar_transplante(self.lista_cirujanos[i], receptor, organo) #si encuentra un cirujano que coincida y esté disponible sale de la función
                    
        #Si no encuentra un especialista disponible, asigna al primer cirujano disponible, no importa especialidad        
        for i in range (len(self.lista_cirujanos)):
            self.lista_cirujanos[i].determinar_disponibilidad(fecha_transplante)
            if (self.lista_cirujanos[i].estado):
                self.lista_cirujanos[i].fecha_ultima_operacion = fecha_transplante
                return self.realizar_transplante(self, self.lista_cirujanos[i], receptor, organo)
                
        #Despues podriamos cambiar esta funcion para priorizar a los cirujanos generales en caso de que no
        #haya un especialista

    def chequear_disponibilidad_cirujano(self):
        cont = 0
        for i in range (len(self.lista_cirujanos)):
            if self.lista_cirujanos[i].estado == True:
                cont += 1
        if cont > 0:
            return True
        else:
            return False