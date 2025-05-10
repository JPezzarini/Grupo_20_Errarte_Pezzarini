from pacientes import Paciente
from centro_de_salud import Centro_Salud
from sistema import Sistema
from donantes import *
from receptores import Receptor
from organo import Organo
from vehiculo import Vehiculo
from ambulancia import Ambulancia
from avion import Avion
from helicoptero import Helicoptero
from cirujano import *
from organo import *


vehiculos1 = [Avion(90), Helicoptero(100), Ambulancia(110), Ambulancia(85), Ambulancia(95)]
vehiculos2 = [Avion(80), Avion(120), Helicoptero(100), Ambulancia(105), Ambulancia(90)]

#Cirujanos
gomez = Cirujano(Especialidad(5))
fischer = Cirujano(Especialidad(1))
fernandez = Cirujano(Especialidad(2))
lopez = Cirujano(Especialidad(3))
# Centros de Salud
cs1 = Centro_Salud("Hospital Central", "La Plata", "Buenos Aires", "+54 911 1234-5678", [gomez, fischer], vehiculos1)
cs2 = Centro_Salud("Clínica del Sur", "Avellaneda", "Buenos Aires", "+54 911 8765-4321", [fernandez, lopez], vehiculos2)

# Donantes (10 por centro)
donantes = [
    Donante("Matías", 47391713, datetime(1990, 5, 12), "M", "+54 911 1111-1111", "A+", cs1, datetime(2025, 4, 20), [Organo(Tipo(1)), Organo(7)]),
    Donante("Lucía", 40123567, datetime(1985, 8, 24), "F", "+54 911 2222-2222", "B-", cs1, datetime(2025, 3, 15), [ Organo(Tipo(8))]),
    Donante("Javier", 38912222, datetime(1978, 1, 10), "M", "+54 911 3333-3333", "AB+", cs1, datetime(2025, 2, 5), [Organo(Tipo(2))]),
    Donante("Clara", 42543123, datetime(1992, 12, 2), "F", "+54 911 4444-4444", "O-", cs1, datetime(2025, 1, 30), [Organo(Tipo(1)), Organo(Tipo(9))]),
    Donante("Pedro", 37788990, datetime(1983, 6, 19), "M", "+54 911 5555-5555", "O+", cs1, datetime(2025, 4, 1), [Organo(Tipo(7))]),
    Donante("Martina", 43678123, datetime(1995, 3, 11), "F", "+54 911 6666-6666", "A-", cs2, datetime(2025, 3, 5), [Organo(Tipo(8))]),
    Donante("Esteban", 41872912, datetime(1979, 9, 25), "M", "+54 911 7777-7777", "B+", cs2, datetime(2025, 2, 28), [Organo(Tipo(1))]),
    Donante("Sofía", 40789123, datetime(1986, 4, 14), "F", "+54 911 8888-8888", "AB-", cs2, datetime(2025, 1, 20), [Organo(Tipo(7)), Organo(Tipo(2))]),
    Donante("Tomás", 42345678, datetime(1991, 7, 7), "M", "+54 911 9999-9999", "A+", cs2, datetime(2025, 3, 14), [ Organo(Tipo(9))]),
    Donante("Julieta", 41234567, datetime(1994, 11, 18), "F", "+54 911 0000-0000", "O+", cs2, datetime(2025, 4, 7), [Organo(Tipo(8)), Organo(Tipo(1))]),
]

# Recepieltores (10 por centro)
receptores = [
    Receptor("Ana", 41321789, datetime(1989, 6, 10), "F", "+54 911 1231-4567", "A+", cs1, Organo(Tipo(1)), datetime(2024, 5, 8), "Insuficiencia cardíaca", "Crítico"),
    Receptor("Diego", 40111222, datetime(1975, 3, 22), "M", "+54 911 2342-5678", "B-", cs1, Organo(Tipo(7)), datetime(2023, 12, 10), "Insuficiencia renal", "Estable"),
    Receptor("Laura", 42223333, datetime(1990, 9, 18), "F", "+54 911 3453-6789", "O-", cs1, Organo(Tipo(8)), datetime(2024, 1, 15), "Hepatitis", "Urgente"),
    Receptor("Federico", 43334444, datetime(1982, 2, 5), "M", "+54 911 4564-7890", "AB+", cs1, Organo(Tipo(2)), datetime(2023, 6, 1), "Fibrosis quística", "Estable"),
    Receptor("Sabrina", 44445555, datetime(1996, 11, 11), "F", "+54 911 5675-8901", "O+", cs1, Organo(Tipo(9)), datetime(2024, 3, 20), "Diabetes", "Crítico"),
    Receptor("Nicolás", 45556666, datetime(1988, 8, 29), "M", "+54 911 6786-9012", "A-", cs2, Organo(Tipo(7)), datetime(2023, 11, 5), "Insuficiencia renal", "Urgente"),
    Receptor("Florencia", 46667777, datetime(1979, 5, 13), "F", "+54 911 7897-0123", "B+", cs2, Organo(Tipo(8)), datetime(2024, 2, 25), "Hepatitis", "Estable"),
    Receptor("Joaquín", 47778888, datetime(1984, 10, 6), "M", "+54 911 8908-1234", "AB-", cs2, Organo(Tipo(1)), datetime(2023, 9, 18), "Enfermedad cardíaca", "Crítico"),
    Receptor("Camila", 48889999, datetime(1993, 7, 1), "F", "+54 911 9019-2345", "A+", cs2, Organo(Tipo(2)), datetime(2024, 4, 10), "Fibrosis quística", "Urgente"),
    Receptor("Marcos", 49990000, datetime(1991, 12, 3), "M", "+54 911 0120-3456", "O-", cs2, Organo(Tipo(9)), datetime(2023, 8, 30), "Diabetes", "Estable"),
]

Incucai = Sistema(receptores,donantes,[cs1,cs2])
aaa = Receptor("Ana", 41321789, datetime(1989, 6, 10), "F", "+54 911 1231-4567", "A+", cs1, Organo(Tipo(1)), datetime(2024, 5, 8), "Insuficiencia cardíaca", "Crítico")
organo1 = Organo(Tipo(1))
organo2 = Organo(Tipo(8))

cs1.realizar_transplante(fischer, aaa, organo1)