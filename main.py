from personas.pacientes import Paciente
from centro_de_salud import Centro_Salud
from sistema import Sistema
from personas.donantes import *
from personas.receptores import Receptor
from organo import Organo
from vehiculos.vehiculo import Vehiculo
from vehiculos.ambulancia import Ambulancia
from vehiculos.avion import Avion
from vehiculos.helicoptero import Helicoptero
from personas.cirujano import *
from organo import *
import csv
import random
vehiculos1 = [Avion(90), Helicoptero(100), Ambulancia(110), Ambulancia(85), Ambulancia(95)]
vehiculos2 = [Avion(80), Avion(120), Helicoptero(100), Ambulancia(105), Ambulancia(90)]
#Cirujanos
gomez = Cirujano(Especialidad(5))
fischer = Cirujano(Especialidad(1))
fernandez = Cirujano(Especialidad(2))
lopez = Cirujano(Especialidad(3))
# Centros de Salud
cs1 = Centro_Salud("Hospital Central", "La Plata", "Buenos Aires", "+54 911 1234-5678",[gomez, fischer], vehiculos1)
cs2 = Centro_Salud("Clínica del Sur", "Avellaneda", "Buenos Aires", "+54 911 8765-4321", [fernandez, lopez], vehiculos2)

# Donantes (10 por centro)
donantes = [
    Donante("Matías", 47391714, datetime(1990, 5, 12), "M", "+54 911 1111-1111", "A+", cs1, datetime(2025, 4, 20), [Organo(Tipo(1)), Organo(7)]),
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

# Receptores (10 por centro)
receptores = [
    Receptor("Ana", 41321789, datetime(1989, 6, 10), "F", "+54 911 1231-4567", "A+", cs1, Organo(Tipo(1)), datetime(2024, 5, 8), "Insuficiencia cardíaca", "Inestable"),
    Receptor("Diego", 40111222, datetime(1975, 3, 22), "M", "+54 911 2342-5678", "B-", cs1, Organo(Tipo(7)), datetime(2023, 12, 10), "Insuficiencia renal", "Estable"),
    Receptor("Laura", 42223333, datetime(1990, 9, 18), "F", "+54 911 3453-6789", "O-", cs1, Organo(Tipo(8)), datetime(2024, 1, 15), "Hepatitis", "Estable"),
    Receptor("Federico", 43334444, datetime(1982, 2, 5), "M", "+54 911 4564-7890", "AB+", cs1, Organo(Tipo(2)), datetime(2023, 6, 1), "Fibrosis quística", "Estable"),
    Receptor("Sabrina", 44445555, datetime(1996, 11, 11), "F", "+54 911 5675-8901", "O+", cs1, Organo(Tipo(9)), datetime(2024, 3, 20), "Diabetes", "Inestable"),
    Receptor("Nicolás", 45556666, datetime(1988, 8, 29), "M", "+54 911 6786-9012", "A-", cs2, Organo(Tipo(7)), datetime(2023, 11, 5), "Insuficiencia renal", "Estable"),
    Receptor("Florencia", 46667777, datetime(1979, 5, 13), "F", "+54 911 7897-0123", "B+", cs2, Organo(Tipo(8)), datetime(2024, 2, 25), "Hepatitis", "Estable"),
    Receptor("Joaquín", 47778888, datetime(1984, 10, 6), "M", "+54 911 8908-1234", "AB-", cs2, Organo(Tipo(1)), datetime(2023, 9, 18), "Enfermedad cardíaca", "Estable"),
    Receptor("Camila", 48889999, datetime(1993, 7, 1), "F", "+54 911 9019-2345", "A+", cs2, Organo(Tipo(2)), datetime(2024, 4, 10), "Fibrosis quística", "Estable"),
    Receptor("Marcos", 49990000, datetime(1991, 12, 3), "M", "+54 911 0120-3456", "O-", cs2, Organo(Tipo(9)), datetime(2023, 8, 30), "Diabetes", "Estable"),
]

Incucai = Sistema([cs1,cs2],receptores, donantes)
def mostrar_menu():
    print("1. Crear un paciente")
    print("2. Crear un cirujano")
    print("3. Imprimir lista de donantes")
    print("4. Imprimir lista de receptores")
    print("5. Imprimir receptores de un centro de salud específico")
    print("6. Imprimir donantes de un centro de salud específico")
    print("7. Informar prioridad de un receptor")
    print("8. Salir")
def opcion_1():
    flag = False
    while flag == False:
        try:
            centro_de_salud = str(input("Ingrese el nombre del centro de salud del paciente: "))
            cont = 0
            for i in range(len(Incucai.lista_centros)):
                if (centro_de_salud == Incucai.lista_centros[i].nombre):
                    Incucai.crear_paciente(Incucai.lista_centros[i])
                    cont+=1
            if (cont == 0):
                raise ValueError("Ingreso inválido. No se encontró el centro de salud")
        except ValueError as e:
            print(e)
        else:
            flag = True

def opcion_2():
    flag = False
    while flag == False:
        try:
            centro_de_salud = str(input("Ingrese el nombre del centro de salud del cirujano: "))
            cont = 0
            for i in range(len(Incucai.lista_centros)):
                if (centro_de_salud == Incucai.lista_centros[i].nombre):
                    Incucai.crear_cirujano(Incucai.lista_centros[i])
                    cont+=1
            if (cont == 0):
                raise ValueError("Ingreso inválido. No se encontró el centro de salud")
        except ValueError as e:
            print(e)
        else:
            flag = True

def opcion_3():
    Incucai.listar_donantes()

def opcion_4():
    Incucai.listar_receptores()

def opcion_5():
    flag = False
    while flag == False:
        try:
            centro_de_salud = str(input("Ingrese el nombre del centro de salud: "))
            cont = 0
            for i in range(len(Incucai.lista_centros)):
                if (centro_de_salud == Incucai.lista_centros[i].nombre):
                    cont+=1
            if (cont == 0):
                raise ValueError("Ingreso inválido. No se encontró el centro de salud")
        except ValueError as e:
            print(e)
        else:
            Incucai.buscar_receptores_centro_salud(centro_de_salud)
            flag = True

def opcion_6():
    flag = False
    while flag == False:
        try:
            centro_de_salud = str(input("Ingrese el nombre del centro de salud: "))
            cont = 0
            for i in range(len(Incucai.lista_centros)):
                if (centro_de_salud == Incucai.lista_centros[i].nombre):
                    cont+=1
            if (cont == 0):
                raise ValueError("Ingreso inválido. No se encontró el centro de salud")
        except ValueError as e:
            print(e)
        else:
            Incucai.buscar_donantes_centro_salud(centro_de_salud)
            flag = True
def opcion_7():
    flag = False
    while flag == False:
        try:
            dni = int(input("Ingrese el DNI del receptor para saber su prioridad: "))
            cont = 0
            for i in range(len(Incucai.lista_receptores)):
                if (Incucai.lista_receptores[i].get_dni() == dni):
                    cont+= 1
            if (cont==0):
                raise ValueError("Ingreso inválido. No se encontró el DNI")
        except ValueError as e:
            print(e)
        else:
            Incucai.informar_prioridad_receptor(dni)
            flag = True
def main():
    while True:
        mostrar_menu()
        seleccion = input("Ingrese una opción: ")
        if seleccion == '1':
            opcion_1()
        elif seleccion == '2':
            opcion_2()
        elif seleccion == '3':
            opcion_3()
        elif seleccion == '4':
            opcion_4()
        elif seleccion == '5':
            opcion_5()
        elif seleccion == '6':
            opcion_6()
        elif seleccion == '7':
            opcion_7()
        elif seleccion == '8':
            print("Gracias por utilizar el programa.")
            break
        else:
            print("Opción inválida. Ingrese un número permitido.")
if __name__ == "__main__":
    main()
#def cargar_pacientes_desde_csv(archivo_csv: str):
#    pacientes = []
#    with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
#        lector = csv.DictReader(archivo)
#        for fila in lector:
#
#            paciente = Receptor(
#                nombre=fila['\ufeffnombre'],
#                dni=int(fila['dni']),
#                fecha_nac=datetime.strptime(fila['fecha_nac'], '%Y-%m-%d'),
#                sexo=fila['sexo'],
#                tel=fila['tel'],
#                t_sangre=fila['t_sangre'],
#                centro_salud=fila['centro_salud'],
#                organo_r=fila['organo_r'],
#                dt_espera=datetime.strptime(fila['dt_espera'], '%Y-%m-%d %H:%M:%S'),
#                patologia=fila['patologia'],
#                estado=fila['estado']
#            )
#            pacientes.append(paciente)
#    return pacientes
#pacientes= cargar_pacientes_desde_csv('Archivo_Receptores.csv')
#for paciente in pacientes:
#    print(paciente.get_nombre())
#
#lista_centros=[cs1, cs2]
#def cargar_centros(lista_receptores,lista_centros):
#    for receptor in lista_receptores:
#        receptor.centro_salud=lista_centros[random.randint(0,1)]
#cargar_centros(pacientes, lista_centros)
#for paciente in pacientes:
#    print("\n")
#    print(paciente.centro_salud.nombre)
#
#def cargar_organos(lista_receptores):
#    for receptor in lista_receptores:
#        receptor.organo_r=Organo(tipo=random.randint(1,9))
#cargar_organos(pacientes)
#for paciente in pacientes:
#    print("\n")
#    print(paciente.organo_r.get_tipo())
#
#Incucai.informar_prioridad_receptor(40111222)