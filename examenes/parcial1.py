
class Estudiantes ():
    def __init__ (self, nombre_ingresado, edad_ingresada, genero_ingreado, colegio_graduado):
        self.nombre = nombre_ingresado
        self.edad = edad_ingresada
        self.genero = genero_ingreado
        self.colegios = colegio_graduado
    def asistir (self, cantidad_de_clases):
        for i in range (cantidad_de_clases):
            print ("Hola soy {} y tengo la asistencia numero {}".format(self.nombre,i+1))

class Profesores ():
    def __init__(self, nombre_profe, edad_profe, nivel_profe):
        self.name = nombre_profe
        self.age = edad_profe
        self.nivel = nivel_profe
    def dictar (self, clases_dara):
        for i in range (clases_dara):
            print ("Hola a todos soy el profesor {} y voy a dar la clase numero {}".format(self.name,i+1))
        
class Director (Profesores):
    def contratar (self, cuantos_contrato):
        for i in range (cuantos_contrato):
            print ("Hola soy el director David y voy a contratar",i+2,"profesores de mate")
        

estudiante1 = Estudiantes ("Daniel", 20, "masculino", "JPG")
estudiante1.asistir (5)

estudiantes2 = Estudiantes ("camila", 18, "femenino", "PJB")
estudiantes2.asistir (2)
estudiante3 = Estudiantes ("Tomas", 15, "Masculino", "INMA")
estudiante4 = Estudiantes ("Sofi", 21, "Femanino", "TERE")
estudiante5 = Estudiantes ("Santi", 20, "Masculino", "PJB")

profesor1 = Profesores ("Armando", 30, "Doctorado")
profesor1.dictar (2)
profesor2 = Profesores ("Roberto", 40, "Maestria")
profesor2.dictar (1)

director1 = Director ("David", 50, "Majister")
director1.contratar (1)

#----------------Variables--------------------------#
estudiantes_nombres = ["Daniel", "Camila","Tomas", "Sofi", "Santi"]
estudiantes_edades = [20, 18, 15, 21, 20]
estudiante_genero = ["Masculino", "Femenino", "maculino","femanino","masculinno"]

profe_nombre = ["Armando", "Roberto"]
profe_edad = [30,40]
#---------------------------------------------------#
Mensaje_pregunta = """
    1. Mostrar atributos de los estudiantes 
    2. Mostrar los atributos de los profesores
    3. Mostrar los atributos del director
    4. salir
"""

def mostrar_tres_listas (lista1,lista2,lista3):
    size_lista1 = len(lista1)
    size_lista2 = len(lista2)
    size_lista3 = len(lista3)
    if (size_lista1==size_lista2==size_lista3):
        for i in range(size_lista1,size_lista2):
            print(lista1[i],lista2[i],lista3[i])
    else:
        print ("las listas no se pueden mostrar juntas")
def mostar_dos_listas (lista1,lista2):
    size_lista1 = len(lista1)
    size_lista2 = len(lista2)
    if (size_lista1==size_lista2):
        for i in range(size_lista1):
            print(lista1[i],lista2[i])
    else:
        print ("las listas no se pueden mostrar juntas")
    

_eleccion_estudiante = 0
while (_eleccion_estudiante!=4):
    _eleccion_estudiante = int(input(Mensaje_pregunta))
    if (_eleccion_estudiante==1):
        mostrar_tres_listas (estudiantes_nombres, estudiantes_edades, estudiante_genero)
    elif (_eleccion_estudiante==2):
        mostar_dos_listas (profe_nombre,profe_edad)
   

    


