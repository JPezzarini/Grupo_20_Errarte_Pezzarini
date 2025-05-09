from organo import Organo

class Cirujano:

    def __init__(self, especialidad):
        self.especialidad = especialidad

    def chequear_especialidad(self, organo: Organo):
        if(self.especialidad == organo._tipo):
            return True
        else:
            return False