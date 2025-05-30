from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from datetime import *
from personas.donantes import Donante
from personas.receptores import Receptor
from vehiculos.vehiculo import Vehiculo
import random
from otros.organo import *
from excepciones.error import *
from personas.cirujano import *
if TYPE_CHECKING:
    from personas.pacientes import Paciente
    from otros.centro_de_salud import Centro_Salud
    from vehiculos.ambulancia import Ambulancia
    from vehiculos.avion import Avion
    from vehiculos.helicoptero import Helicoptero
    

class Sistema():

    """
    Esta clase representa el sistema operativo de INCUCAI
    """

    def __init__(self, centros_salud: list[Centro_Salud], lista_receptores: list[Receptor], lista_donantes: list[Donante]):
        self.lista_receptores = lista_receptores
        self.lista_donantes = lista_donantes
        self.lista_centros = centros_salud



    def recibir_paciente(self, paciente) -> None:
        """
        Agrega un paciente al sistema, determinando si es donante o receptor.
        Llama a las funciones recibir_donante y recibir_receptor.

        Params:
            - paciente (Paciente): El paciente a agregar.

        Precon:
            El paciente debe ser instanciado como Donante o Receptor, puesto que
            paciente es una clase abstracta.

        Returns:
            None.
        """

        if isinstance(paciente, Donante):
            self.recibir_donante(paciente)
        else:
            self.recibir_receptor(paciente)


    def recibir_donante(self, donante: Donante) -> None:
        """
        Agrega un donante al sistema y busca match con los receptores del mismo.
        Llama a la función buscar_match_donante
        Params:
            - donante (Donante): El donante a agregar.

        Returns:
            None.
         """

        self.lista_donantes.append(donante)
        i=0
        while i < (len(donante.lista_organos)):
            k = i
            self.buscar_match_donante(donante,donante.lista_organos[i],k)
            i+=1

    def recibir_receptor(self, receptor: Receptor) -> None:
        """
        Agrega un receptor al sistema y busca match con los donantes del mismo.
        Llama a la función buscar_match_receptor
        Params:
            - receptor (Receptor): El receptor a agregar.

        Returns:
            None.
        """

        self.lista_receptores.append(receptor)
        self.buscar_match_receptor(receptor)
    

    def elegir_receptor(self, receptores: list[Receptor]) -> Receptor:
        """
        Ordena la lista de receptores compatibles según su prioridad de manera descendente.
        Llama a la función elegir_receptor_prioridad.

        Params:
            - receptores (list[Receptor]): La lista de receptores compatibles con el órgano del donante.

        Returns:
            un objeto de tipo Receptor que representa el receptor de mayor prioridad en la lista.
        """
        
        for i in range(len(receptores)):
            for k in range (0,len(receptores)-1-i):
                if(receptores[k+1].prioridad > receptores[k].prioridad):
                    a = receptores[k]
                    receptores[k] = receptores[k+1]
                    receptores[k+1] = a
        receptor_match = self.elegir_receptor_prioridad(receptores)
        return receptor_match


    def elegir_receptor_prioridad(self, receptores: list[Receptor]) -> Receptor:
        """
        Ordena la lista de receptores. En caso de tener la misma prioridad, los ordena por tiempo de ingreso en el sistema
        de manera descendiente.

        Params:
            - receptores (list[Receptor]): La lista de receptores compatibles con el órgano del donante.

        Returns:
            un objeto de tipo Receptor que representa el receptor de mayor prioridad en la lista.
        """

        for i in range(len(receptores)):
            for k in range (0,len(receptores)-1-i):
                if(receptores[k+1].dt_espera > receptores[k].dt_espera and receptores[k+1].prioridad == receptores[k].prioridad):
                    a = receptores[k]
                    receptores[k] = receptores[k+1]
                    receptores[k+1] = a
        return receptores[0]
    


    def buscar_match_donante(self,donante: Donante,organo: Organo, k: int) -> None:
        """
        Busca receptores compatibles según el donante y el órgano especificado.
        En caso de encontrar un match, busca un transporte y cirujano disponibles.  
        Llama a la funcion elegir_receptor, asignar_vehiculo y asignar_cirujano.

        Params:
            - donante (Donante): Un donante del sitema.
            - organo (Organo): El órgano a donar.
            - k (int): Un índice que representa la posición del órgano en la lista de órganos del donante.

        Returns:
            None
        """

        receptores = []
        for i in range(len(self.lista_receptores)):
            if(self.lista_receptores[i].organo_r.get_tipo() == organo.get_tipo() and self.lista_receptores[i].get_t_sangre() == donante.get_t_sangre()):
                receptores.append(self.lista_receptores[i])
    
        if(len(receptores) == 0):
            print("No se encontraron receptores que cualifiquen") #printea si no encuentra match
            return
        
        receptor_match = self.elegir_receptor(receptores) #receptor de mayor prioridad
        
        try:
            if(receptor_match.centro_salud.chequear_disponibilidad_cirujano() == False):
                raise DisponibilidadError("No hay cirujanos disponibles para realizar la operación")
        except DisponibilidadError as e:
            print(e)
        else:
            hoy = date.today()
            donante.lista_organos[k].dt_ablacion = datetime.combine(hoy,time(random.randint(0,23),random.randint(0,59),random.randint(0,59))) # creo una fecha y tiempo de ablacion random
            fecha_ablacion = donante.lista_organos[k].dt_ablacion #guarda la fecha en una variable para pasarla entre funciones
            viaje = f"{donante.centro_salud.nombre}-{receptor_match.centro_salud.nombre}" #guarda el viaje para pasarselo al vehiculo
            if(receptor_match.centro_salud == donante.centro_salud):
                if (receptor_match.centro_salud.asignar_cirujano(receptor_match, donante.lista_organos[k])): #si sale bien se retira el organo y se retira el receptor de la lista
                    self.lista_receptores.remove(receptor_match)
                    donante.lista_organos.remove(organo)
                else: #si sale mal se pierde el organo y el receptor pasa a estar inestable
                    donante.lista_organos.remove(organo)
                    receptor_match.estado = "inestable"
            
            else:
                if(donante.centro_salud.asignar_vehiculo(receptor_match.centro_salud,viaje,fecha_ablacion)):
                    if (receptor_match.centro_salud.asignar_cirujano(receptor_match, donante.lista_organos[k])): #si sale bien se retira el organo y se retira el receptor de la lista
                        self.lista_receptores.remove(receptor_match)
                        donante.lista_organos.remove(organo)
                    else: #si sale mal se pierde el organo y el receptor pasa a estar inestable
                        donante.lista_organos.remove(organo)
                        receptor_match.estado = "inestable"
            

    def buscar_match_receptor(self, receptor: Receptor) -> None:
        """
        Busca un donante compatible para el receptor especificado.
        En caso de encontrar un match, busca un transporte y cirujano disponibles. 
        Llama a la funcion elegir_receptor, asignar_vehiculo y asignar_cirujano.

        Params:
            - receptor (Receptor): Un receptor del sistema.

        Precon (opcional):
            El receptor debe ser una instancia válida de Receptor.

        Returns:
            None.
        """

        i = 0
        cont = 0 
        while i < (len(self.lista_donantes)):
            k=0
            while k < (len(self.lista_donantes[i].lista_organos)):
                if(receptor.organo_r.get_tipo() == self.lista_donantes[i].lista_organos[k].get_tipo() and receptor.get_t_sangre() == self.lista_donantes[i].get_t_sangre()):
                    cont += 1
                    try:    
                        if (receptor.centro_salud.chequear_disponibilidad_cirujano() == False):
                            raise DisponibilidadError("No hay cirujanos disponibles para realizar la operación")
                    except DisponibilidadError as e:
                        print(e)
                    else:
                        hoy = date.today()
                        self.lista_donantes[i].lista_organos[k].dt_ablacion = datetime.combine(hoy,time(random.randint(0,23),random.randint(0,59),random.randint(0,59))) # creo una fecha y tiempo de ablacion random
                        fecha_ablacion = self.lista_donantes[i].lista_organos[k].dt_ablacion #guardo la fecha en una variable para pasarla entre funciones
                        viaje = f"{self.lista_donantes[i].centro_salud.nombre}-{receptor.centro_salud.nombre}" #me guardo el viaje para pasarselo al vehiculo 
                        if(self.lista_donantes[i].centro_salud == receptor.centro_salud):
                            if (receptor.centro_salud.asignar_cirujano(receptor, self.lista_donantes[i].lista_organos[k])): #si sale bien se retira el organo y se retira el receptor de la lista
                                self.lista_receptores.remove(receptor)
                            else: #si sale mal se pierde el organo y el receptor pasa a estar inestable
                                receptor.estado = "inestable"
                            self.lista_donantes[i].lista_organos.pop(k)
                            if (self.lista_donantes[i].lista_organos): #Si el donante ya no tiene más organos se retira al donante de la lista
                                self.lista_donantes.pop(i)
                            return
                        
                        else:
                            if(self.lista_donantes[i].centro_salud.asignar_vehiculo(receptor.centro_salud,viaje,fecha_ablacion)):
                                if (receptor.centro_salud.asignar_cirujano(receptor, self.lista_donantes[i].lista_organos[k])): #si sale bien se retira el organo y se retira el receptor de la lista
                                    self.lista_receptores.remove(receptor)
                                else: #si sale mal se pierde el organo y el receptor pasa a estar inestable
                                    receptor.estado = "inestable"
                                self.lista_donantes[i].lista_organos.pop(k)
                                if (self.lista_donantes[i].lista_organos): #Si el donante ya no tiene más organos se retira al donante de la lista
                                    self.lista_donantes.pop(i)
                                return
                k+=1
            i+= 1
        if ( cont == 0):
            print("No se encontraron donantes compatibles")


    def crear_paciente(self, centro_salud: Centro_Salud) -> None:
        """
        Crea un nuevo paciente por consola y lo agrega al sistema.

        Params:
            - centro_salud (Centro_Salud): Centro de salud al que pertenecerá el paciente.

        Returns:
            None.
        """

        nombre = str(input("Ingrese el nombre del paciente: "))
        flag = False
        while flag == False:
            try:
                dni = int(input("Ingrese el DNI del paciente: "))
                for i in range(len(self.lista_receptores)):
                    if(self.lista_receptores[i].get_dni() == dni):
                        raise DniError("Entrada inválida, DNI ya registrado")
                for i in range(len(self.lista_donantes)):
                    if(self.lista_donantes[i].get_dni() == dni):
                        raise DniError("Entrada inválida, DNI ya registrado")    
            except DniError as e:
                print(e)
            except ValueError:
                print("Entrada inválida, ingrese sólo números")
            else:
                flag = True

        flag = False
        while flag == False:
            str_nacimiento = str(input("Ingrese su fecha de nacimiento  AAAA-MM-DD: "))
            try:
                fecha_nacimiento = datetime.strptime(str_nacimiento,"%Y-%m-%d")
            except ValueError:
                print("Formato de fecha inválido, ingréselo devuelta")
            else:
                flag = True

        flag = False
        while flag == False:
            try:
                sexo = str(input("Ingrese el sexo del paciente, Masculino = M, Femenino = F: ").strip().upper())
                if sexo not in ("M", "F"):
                   raise ValueError("Entrada inválida, solo se acepta 'M' o 'F'.")
            except ValueError as e:
                print(e)
            else:
                flag = True
        flag = False
        while flag == False:
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
            else:
                flag = True
        flag = False
        while flag == False:
            try:
                tipo_sangre = str(input("Ingrese su tipo de sangre: "))
                if tipo_sangre not in ("A+","A-","B+","B-","O+","O-","AB+","AB-"):
                   raise ValueError("Entrada inválida, tipo de sangre no existente")
            except ValueError as e:
                print(e)
            else:
                flag = True  
        flag = False  
        while flag == False:
            try:
                tipo_paciente = input("Su paciente es donante o receptor? Donante = D; Receptor = R: ")
                if tipo_paciente not in ("D", "R"):
                   raise ValueError("Entrada inválida, tipo de paciente no existente")
            except ValueError as e:
                print(e)
            else:
                flag = True

        if (tipo_paciente == "D"):
            flag = False
            while flag == False:
                str_fallecimiento = str(input("Ingrese la fecha de fallecimiento  AAAA-MM-DD: "))
                try:
                    dt_fallecimiento = datetime.strptime(str_fallecimiento,"%Y-%m-%d")
                except ValueError:
                    print("Formato de fecha inválido, ingréselo devuelta")
                else:
                    hora = int(input("Ingrese la hora (0-23): "))
                    minutos = int(input("Ingrese los minutos (0-59): "))
                    dt_fallecimiento = dt_fallecimiento.replace(hour = hora, minute = minutos)
                    flag = True
            flag = False
    
            lista_organos = []
            cantidad_organos = int(input("ingrese la cantidad de organos: "))
            for i in range (0,cantidad_organos):
                flag = False
                while flag == False:
                    try:
                        tipo = str(input("ingrese el tipo de organo: ")).strip().lower()
                        if tipo not in ("corazón","pulmón","piel","córnea","hueso","intestino","riñón","hígado", "páncreas"):
                           raise ValueError("Entrada inválida, órgano no admitido")
                    except ValueError as e:
                        print(e)
                    else: 
                        flag = True
                organo_i = Organo(Tipo[tipo])
                lista_organos.append(organo_i)
            paciente = Donante(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud, dt_fallecimiento, lista_organos)

        else:
            flag = False
            while flag == False:
                try:
                    tipo = str(input("ingrese el tipo de organo: ")).strip().lower()
                    if tipo not in ("corazón","pulmón","piel","córnea","hueso","intestino","riñón","hígado", "páncreas"):
                       raise ValueError("Entrada inválida, órgano no admitido")
                except ValueError as e:
                    print(e)
                else: 
                    flag = True
            organo_r = Organo(Tipo[tipo])
            flag = False
            while flag == False:
                str_espera = str(input("Ingrese la fecha de ingreso al sistema  AAAA-MM-DD: "))
                try:
                    dt_espera = datetime.strptime(str_espera,"%Y-%m-%d")
                except ValueError:
                    print("Formato de fecha inválido, ingréselo devuelta")
                else:
                    flag = True
            flag = False
            patologia = str(input("ingrese su patologia: "))
            while flag == False:
                try:
                    estado = str(input("ingrese su estado: "))
                    if estado not in ("estable", "inestable"):
                       raise ValueError("Entrada inválida, estado invalido")
                except ValueError as e:
                    print(e)
                else:
                    flag = True
            flag = False
            paciente = Receptor(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud, organo_r, dt_espera, patologia,estado)
        print("El paciente fue creado con éxito. Se lo recibirá y se buscarán las compatibilidades de todos los pacientes del sistema")
        self.recibir_paciente(paciente)

    def crear_cirujano(self, centro_salud: Centro_Salud) -> None:
        """
        Crea un nuevo cirujano por consola y lo agrega a la lista del centro de salud especificado.

        Params:
            - centro_salud (Centro_Salud): El centro de salud al que pertenecerá el cirujano.

        Returns:
            None.
        """

        flag = False
        while flag == False:
            try:
                especialidad = str(input("Ingrese su especialidad: "))
                if especialidad not in ("general","cardiovascular","pulmonar","plastico","traumatologo","gastroenterologo"):
                    raise ValueError("Entrada inválida, especialidad no admitida")
            except ValueError as e:
                print(e)
            else:
                flag = True
        cirujano = Cirujano(Especialidad[especialidad])
        centro_salud.lista_cirujanos.append(cirujano)
        print("El cirujano fue creado con éxito")


    def listar_receptores(self) -> None:
        """
        Imprime la lista de receptores del sistema.

        Params:
            None.

        Returns:
            None.
        """

        if self.lista_receptores == False:
            print("No hay receptores en el sistema")
            return
        
        for i in range (len(self.lista_receptores)):
            print(self.lista_receptores[i].__repr__())


    def listar_donantes(self) -> None:
        """
        Imprime la lista de donantes del sistema.

        Params:
            None.

        Returns:
            None.
        """

        if self.lista_donantes == False:
            print("No hay donantes en el sistema")
            return
        
        for i in range (len(self.lista_donantes)):
            print(self.lista_donantes[i].__repr__())
                

    def buscar_receptores_centro_salud(self, centro_de_salud: str) -> None:
        """
        Busca e imprime los receptores asociados a un centro de salud específico.

        Params:
            - centro_de_salud (str): El nombre del centro de salud.

        Returns:
            None
        """
            
        for i in range(len(self.lista_receptores)):
            if (self.lista_receptores[i].centro_salud.nombre == centro_de_salud):
                print(self.lista_receptores[i].__repr__())


    def buscar_donantes_centro_salud(self, centro_de_salud:str) -> None:
        """
        Busca e imprime los donantes asociados a un centro de salud específico.

        Params:
            - centro_de_salud (str): El nombre del centro de salud.

        Returns:
            None
        """

        for i in range(len(self.lista_donantes)):
            if (self.lista_donantes[i].centro_salud.nombre == centro_de_salud):
                print(self.lista_donantes[i].__repr__())

    
    def informar_prioridad_receptor(self, dni_receptor) -> None:
        """
        Busca e informa la prioridad de un receptor según su DNI.

        Params:
            - dni_receptor (int): El DNI del receptor.

        Returns:
            None
        """

        try:
            cont = 0
            for i in range(len(self.lista_receptores)):
                if (self.lista_receptores[i].get_dni() == dni_receptor):
                    print(f"En la escala de prioridad, el paciente se encuentra en el nivel {self.lista_receptores[i].prioridad}")
                    return
            if cont == 0:
                raise EncontrarpacienteError("No se encontró al paciente.")
        except EncontrarpacienteError as e:
            print(e)
                
