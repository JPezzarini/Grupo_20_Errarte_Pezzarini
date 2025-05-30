from personas.pacientes import Paciente
from datetime import *
from otros.organo import Organo
from otros.centro_de_salud import Centro_Salud

class Receptor(Paciente):
    """
    Esta clase representa a un receptor. Hereda los atributos de la clase Paciente.
    """

    def __init__(self, nombre: str, dni: int, fecha_nac: datetime, sexo: str, tel: str, t_sangre: str, centro_salud: Centro_Salud, organo_r : Organo, dt_espera: datetime, patologia: str, estado: str ):
        """
        Inicializa un Receptor.
        
        Atributos:
            - nombre (str): El nombre del receptor.
            - dni (int): El DNI del receptor.
            - fecha_nac (datetime): La fecha de nacimiento del receptor.
            - sexo (str): El sexo del receptor (M/F).
            - tel (str): El número de teléfono del recptor.
            - t_sangre (str): El tipo de sangre del receptor.
            - centro_salud (Centro_Salud): El centro de salud al que está asociado el receptor.
            - organo_r (Organo): El órgano a recibir.
            - dt_espera (datetime): Tiempo desde que ingresó al sistema.
            - patologia (str): La patología del receptor.
            - estado (str): El estado del receptor (estable/inestable).

        returns:
            None.
        """
        super().__init__(nombre, dni, fecha_nac, sexo, tel, t_sangre, centro_salud)
        self.organo_r = organo_r
        self.dt_espera = dt_espera
        self.patologia = patologia
        self.estado = estado
        self.prioridad = self.calcular_prioridad()
        

    def calcular_prioridad(self) -> int:
        """
        Calcula la prioridad del receptor en dependencia de su edad.

        returns:
            Un int que indica la prioridad del paciente en la escala
        """

        if self.estado == "inestable":
            self.prioridad = 10
            return self.prioridad

        else:
            fecha_nacimiento_date = self._fecha_nac.date()
            edad = (date.today() - fecha_nacimiento_date)
            edad = edad.days // 365
            if (edad < 18):
                self.prioridad = 8
            if (edad >=18 and edad<40):
                self.prioridad = 6
            if (edad >= 40 and edad < 65):
                self.prioridad = 4
            if (edad >= 65):
                self.prioridad = 2
        return self.prioridad
            
            
    def __repr__(self) -> None:
        """
        Retorna todos los atributos del donante.
        """
        return f"Nombre: {self._nombre}, DNI: {self._dni}, Fecha de nacimiento: {self._fecha_nac}, Sexo: {self._sexo}, Teléfono: {self.tel}, Sangre: {self._t_sangre}, Centro: {self.centro_salud.nombre}, Organo: {self.organo_r._tipo.name}, Ingreso a la lista de espera: {self.dt_espera}, Patología: {self.patologia}, Estado: {self.estado}"