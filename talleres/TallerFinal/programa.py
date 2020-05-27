import sys
#--------------------------------------------------------------#
MENSAJE__BIENVENIDA ="Bienvenido al programa"

#------------------------------------------------------------------#
import matplotlib.pyplot as plt
import pandas as p

print(MENSAJE__BIENVENIDA)

def validador_archivo (file):
    assert(file)
    return False
validador = True

while (validador):
    file =  input('Escriba el nombre del archivo : ')
    try:
        validador = open (file)
        validador = False
    except FileNotFoundError:
        print("La entrada no es válida")


ecg = p.read_csv(file,encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title(input("ingrese el titulo del grafico : "))
plt.xlabel(input("ingrese el titulo del eje x : "))
plt.ylabel(input("ingrese el titulo del eje y : "))
plt.plot(x,y)
plt.savefig(input("ingrese el nombre de como quiere guardar el grafico : "))
plt.show()

#-----------------------------------------------------------------#
print ("#"*60)

nombre = "\nNo ingresaste el nombre"
try:
    nombre = (input('Ingrese su nombre : '))
except ValueError:
    print ("ingresaste mal el nombre")
print ("Hola", nombre,"procederemos a calcular tu IMC")

edad = "No ingresaste edad"
try:
    edad = int (input('Ingrese su edad : '))
except ValueError:
    print ("ingresaste mal la edad")
print ("Tu edad es", edad)

estatura = "No ingresaste tu estatura"
try:
    estatura = float (input('Ingrese su estatura : '))
except ValueError:
    print ("ingresaste mal la estatura")
print ("Tu estatura es", estatura)

peso = "No ingresaste tu peso"
try:
    peso = float (input('Ingrese su peso : '))
except ValueError:
    print ("ingresaste mal el peso")
print ("Tu peso es", peso)

IMC = ((peso/estatura**2))
print ("Como resultado tu IMC ES : ",IMC)

if ((IMC >= 12) and (IMC<=19)):
    print(MESAJE_PESO_BAJO)
elif((IMC >=19) and (IMC <=25)):
    print(MENSAJE_PESO_SALUDABLE)
elif((IMC >=25) and (IMC <=30)):
    print(MESAJE_SOBREPESO)
else:
    print(MESAJE_OBESIDAD)
#------------------------------------------------------------------#
print ("#"*60)

kilos_arroz= "No ingresaste los kilos de arroz"
try:
    kilos_arroz = float (input('Ingrese los kilos de arroz : '))
except ValueError:
    print ("ingresaste mal los kilos de arroz")
print ("los kilos comprados de arroz fueron", kilos_arroz)

kilos_lentejas = "No ingresaste los kilos de lentejas"
try:
    kilos_lentejas = float (input('Ingrese los kilos de lentejas : '))
except ValueError:
    print ("ingresaste mal los kilos de lentejas")
print ("los kilos comprados de lentejas fueron", kilos_lentejas)

kilos_frijoles = "No ingresaste los kilos de frijoles"
try:
    kilos_frijoles = float (input('Ingrese los kilos de frijoles : '))
except ValueError:
    print ("ingresaste mal los kilos de frijoles")
print ("los kilos comprados de frijoles fueron", kilos_frijoles)

kilos_papa = "No ingresaste los kilos de papa"
try:
    kilos_papa = float (input('Ingrese los kilos de papa : '))
except ValueError:
    print ("ingresaste mal los kilos de papa")
print ("los kilos comprados de papa fueron", kilos_papa)

mercado = {
    "productos" : ["Arroz", "Lentejas", "Frijoles", "Papa"]
}
kilos = (kilos_arroz, kilos_lentejas, kilos_frijoles, kilos_papa)


print (mercado["productos"])
print (kilos)

plt.bar (mercado["productos"], kilos)
plt.title("Productos vs Kilos", fontsize=20)
plt.xlabel("(PRODUCTOS)")
plt.ylabel("(KILOS)")
plt.savefig("ProductosVsKilos.png")
plt.show ()
#------------------------------------------------------------------#
labels = 'Leche', 'Huevo', 'Vino','Arroz','Queso','Salchichas'
sizes = [12, 8, 4, 26, 30, 20]
explode = (0, 0, 0, 0, 0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("% DE COMPRAS")
plt.savefig("Grafico_Compras.png")
plt.show()

#---------------------------------------------------------------------#
def validador_parrafo (parrafo):
    assert(parrafo.endswith("."))
    return False
validador = True

while (validador):
    parrafo =  input('Escriba como se ha sentido con las compras, debe termine con punto : ')
    try:
        validador = validador_parrafo (parrafo)
    except AssertionError:
        print("La entrada no es válida")
#------------------------------------------------------------------#




