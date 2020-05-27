import sys
#--------------------------------------------------------------#
MENSAJE__BIENVENIDA ="Bienvenido al programa"
MESAJE_PESO_BAJO = "estas bajo de peso"
MENSAJE_PESO_SALUDABLE = "estas saludable"
MESAJE_SOBREPESO = "estas en sobrepeso"
MESAJE_OBESIDAD = "estas en obesidad"
#--------------------------------------------------------------#

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
#-----------------------------------------------------------------------------#

print ("#"*60)

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


#-----------------------------------------------------------------------------#

ppg =p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title("PPG-uV DE PACIENTE DIAGNOSTICADO")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("ppg.png")
plt.show ()

eeg =p.read_csv("eeg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(eeg["muestra"].values())
y = list(eeg["valor"].values())
plt.title("EEG-uV DE PACIENTE DIAGNOSTICADO")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("EEG.png")
plt.show ()

ecg =p.read_csv("ecg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("ECG-uV DE PACIENTE DIAGNOSTICADO")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("ECG.png")
plt.show()

barrios = p.read_csv("picos.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
plt.title("ESTUDIOS vs PICOS", fontsize=20)
plt.bar(barrios["nombre"].values(),barrios["pico"].values(),align="center")
plt.xlabel("Nombres")
plt.ylabel("Picos")
figure = plt.gcf()
figure.set_size_inches(8,8)
plt.savefig("Estudiovspico.png")
plt.show ()
#--------------------------------------------------------------------------------#

labels = 'Sala', 'Cocina', 'Baño','Habitacion','Comedor'
sizes = [15, 15, 15, 40, 15]
explode = (0, 0, 0, 0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("% DE LUGARES")
plt.savefig("Grafico_Lugares.png")
plt.show()
#----------------------------------------------------------------------------------#
print ("#"*60)
print ("""En el aprendizaje supervisado nosotros le damos un conjunto de caracteristicas al clasificador, 
para que el preste atencion a esos datos y el decide que tipo de objeto es. En el aprendizaje no 
supervisado tambien llamado inteligencia artificial, es donde la maquina agrupa segun las caracteristicas 
detectadas teniendo en cuanta que no sabe a ciencia cierta cuales son los grupos deseados, en otras 
palabras la maquina tiene la capacidad de tomar decisiones.""")
