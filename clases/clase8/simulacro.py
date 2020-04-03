class Canguro ():
    def __init__ (self, identificacion, edad, totalcanguros, saltos):
        self.identificacion = identificacion
        self.edad = edad    
        self.totalcanguros = totalcanguros
        self.saltos = saltos

class Cuidadores ():
    def __init__ (self, identificacion, nombre):
        self.identificacion = identificacion
        self.nombre = nombre 
    
    def alimentar_canguros (self, totalcanguros):
        print ("el cuidador tiene que alimentar {} canguros del zoologico".format(totalcanguros))

class Jefe (Cuidadores):
    def __init__ (self, Cuidadores):
        self.nombre = Cuidadores.nombre
    def contratar_cuidadores (self, nombre):
        print ("yo soy el jefe y contrate a : {} , tengo muy buenas referencias ".format(nombre))
    def mensaje_para_todos (self, memsaje):
        print ("el jefe quiere darle un mensaje a todos los empleados : \n {}".format(memsaje))

canguro1 = Canguro ("Pepe", 10, 1, 11)
canguro2 = Canguro ("Raul", 13, 2, 12)
canguro3 = Canguro ("nene", 15, 3, 13)
canguro4 = Canguro ("niño", 20, 4, 14)
canguro5 = Canguro ("tifo", 12, 5, 15)
canguro6 = Canguro ("Cami", 30, 6, 16)
canguro7 = Canguro ("Avi", 11, 7, 17)
canguro8 = Canguro ("Adri", 16, 8, 18)
canguro9 = Canguro ("Sami", 21, 9, 19)
canguro10 = Canguro ("Rober", 22, 10, 20)

print ("esta es la cantidad de saltos que dio el canguro 5 :")
print (canguro5.saltos)

cuidador1 = Cuidadores (101, "Armando")
cuidador2 = Cuidadores (111, "Camilo")
cuidador3 = Cuidadores (121, "Roberto")
cuidador4 = Cuidadores (131, "Arturo")
cuidador5 = Cuidadores (141, "Daniela")


cuidador4.alimentar_canguros(10)
jefe1 = Jefe(cuidador3)
jefe1.contratar_cuidadores ("Alvaro")
jefe1.mensaje_para_todos("todos estan despedidos")

