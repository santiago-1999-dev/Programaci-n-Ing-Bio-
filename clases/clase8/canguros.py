# Canguros:
#        atributos: edad, id
#        funciones: saltar(cantidad_de_saltos)
#        --> entradas: cantidad_de_saltos = cantidad de saltos del canguro
#        --> salidas :none

class Canguros ():
    def __init__ (self, edad_ingresada, id_ingresado):
        self.edad = edad_ingresada
        self.id = id_ingresado
    def Saltar (self, cantidad_de_saltos):
        for i in range (cantidad_de_saltos):
            print ("Hola a todos soy el canguro de identificacion {} y di mi salto numero {}".format(self.id,i+1))

# Cuidadores:
#        atributos: nombre, id
#        funciones: alimentar_canguros(cantidad_de_canguros)
#                   --> entradas: cantidad_de_canguros = cantidad de canguros a alimentar
#                   --> salidas :none

class Cuidadores ():
    def __init__ (self, name, id_ingresado):
        self.nombre = name
        self.id = id_ingresado
    def alimentar_canguros (self, cantidad_de_canguros):
        for i in range (cantidad_de_canguros):
            print ("Hola a todos soy el cuidador de nombre {} y alimente al canguro numero {}".format(self.nombre,i+1))

#Jefe(Cuidadores)
#        funciones: 
#               contratar(nombre, id)
#                   --> entradas: nombre = nombre del cuidador
#                   --> entradas: id = identificacion del cuidador
#                   --> salida:contratado 
#               dar_mensaje(mensaje)
#                   --> entradas: mensaje = mensaje a mostrar
#                   -->salidas: none

class Jefe (Cuidadores):
    def dar_mensaje (self, mensaje):
        print("hola todos mi nombre es {} y vengo dar el siguiente mensaje".format(self.nombre))
        print (mensaje)
    def contratar (self, id, nombre):
        cuidador = Cuidadores (nombre, id)
        return cuidador


canguro1 = Canguros(27,100)
canguro1.Saltar (4)

cuidador1= Cuidadores("mafer",120)
cuidador1.alimentar_canguros(6)

jefe1= Jefe("Octavio",32)
jefe1.dar_mensaje("Espero que haya servido de algo esta asesoria")

cuidador2 = jefe1.contratar(23,"daniel") 
cuidador2.alimentar_canguros(3)
