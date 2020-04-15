
#--------------------Variables--------------------------------#
estudiantes = ["David", "santiago", "juanes", "lesly"]
estudiantes_edades = [20,19,17,19]
estudiantes_identificaciones = [20,19,17,19]
#-------------------------------------------------------------#
Mensaje_pregunta = """
    1. Desea ingresar la edad, nombre y ID de un nuevo estudiante
    2. Para mostar los nombres de la lista de estudiantes 
    3. Para mostrar lista de nombres y edades
    4. Para ingresar varios estudiantes con edad, nombre y ID hasta que desee parar
    5. salir 
"""
#----------------------Definiciones---------------------------#
def agregar_nuevo_estudiante (lista_nombres, lista_edades, lista_ID):
    nombre = input ("ingrese el nombre del estudiante nuevo : ")
    lista_nombres.append(nombre)
    edad = int (input("ingrese  la edad del estudiante nuevo : "))
    lista_edades.append (edad)
    identificacion = int (input("ingrese la identificacion del estudiante nuevo : "))
    lista_ID.append (identificacion)

def mostrar_lista(lista):
    for elemento in lista:
        print(elemento)

def mostrar_dos_listas(lista1,lista2):
    size_lista1 = len(lista1)
    size_lista2 = len(lista2)
    if (size_lista1==size_lista2):
        for i in range(size_lista1):
            print(lista1[i],lista2[i])
    else:
        print ("las listas no se pueden mostrar juntas")

def agregar_varios(lista_nombres, lista_edades, lista_ID):
    _decision = "s"
    pregunta = """
        s-> Argegar más estudiantes
        n->para salir
    """
    while (_decision != "n"):
        if (_decision =="s"):
            agregar_nuevo_estudiante(lista_nombres,lista_edades,lista_ID)
        else:
            print("entrada no válida")
        _decision = input(pregunta)

#----------------------Codigo------------------------------#
_eleccion_estudiante = 0
while (_eleccion_estudiante!=5):
    _eleccion_estudiante = int(input(Mensaje_pregunta))
    if (_eleccion_estudiante==1):
        agregar_nuevo_estudiante(estudiantes,estudiantes_edades,estudiantes_identificaciones)
    elif (_eleccion_estudiante ==2):
        mostrar_lista(estudiantes)
    elif (_eleccion_estudiante == 3):
        mostrar_dos_listas(estudiantes, estudiantes_edades)
    elif (_eleccion_estudiante == 4):
        agregar_varios(estudiantes,estudiantes_edades,estudiantes_identificaciones)
    elif(_eleccion_estudiante == 5):
        print("Gracias por usar el programa")
    else:
        print("ingrese un número válido")


    

