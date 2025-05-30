
class DniError(Exception):
    """
    Si encuentra dos DNI iguales al intentar crear un paciente, se hace el raise del error
    """
    pass

class DisponibilidadError(Exception):
    """
    Si no encuentra cirujanos disponibles, se hace el raise del error
    """
    pass

class EncontrarpacienteError(Exception):
    """
    Si no se encuentra al paciente solicitado, se hace el raise del error
    """
    pass