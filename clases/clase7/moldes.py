class Humano ():
    def __init__(self, nombre, estatura, edad, genero):
    
        self.raza = "ser humano"
        self.nombre = nombre
        self.estatura = estatura
        self.edad = edad
        self.genero = genero
        print ("hola a todos soy un", self.raza, "mi nombre es", self.nombre)

    def mostras_atributos (self):
        print ("mi nombre es", self.nombre)
        print ("mi estatura es", self.estatura)
        print ("mi genero es", self.genero)
        print ("mi edad es", self.edad)

    def caminar (self, cantidad_pasos):
        for i in range (cantidad_pasos):
            print ("he caminado ", i+1, "pasos")
      
ser_humano_1 = Humano ("Daniel", 1.67, 27, "maculino")
ser_humano_2 = Humano ("Santiago", 1.88, 20,  "masculino")

ser_humano_1.mostras_atributos ()
ser_humano_2.mostras_atributos ()

ser_humano_1.caminar(100)




