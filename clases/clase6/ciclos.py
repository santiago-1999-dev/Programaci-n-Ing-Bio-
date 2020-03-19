# _cantidadSaltos = int (input("ingrese la cantidad de saltos : "))
# for i in range (4):
#     print(i)

# for i in range(_cantidadSaltos):
#     print ("el canguro da su salto numero" ,i+1)

#----------CODIGO------------
# listaDias = ["lunes" ,
# "martes" ,
# "miercoles" , 
# "jueves" , 
# "viernes"]
# for dia in listaDias :
#     print (dia)

#----------CODIGO-------------
NOMBRES = ["octavio", "lucas", "abel", "isabella", "kathe", "maria"]
EDADES = [14, 18, 22, 26, 34, 38]
print(len(NOMBRES), len(EDADES))
for i in range (len(NOMBRES)):
    if EDADES [i] >= 18 :
        print (i,"la persona", NOMBRES [i], "es mayor")

sumaEdades = 0
for edad in EDADES :
    sumaEdades = sumaEdades + edad 
print (sumaEdades)