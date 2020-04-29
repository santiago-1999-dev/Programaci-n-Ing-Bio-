import pandas as p
diccionario =p.read_csv("barrios.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict()
print(diccionario)
print(diccionario.keys())
print(diccionario["Barrio"])


mayor_nombre = max (diccionario["Barrio"].values(), key=len)
minimo_nombre = min (diccionario["Barrio"].values(), key=len)

print("\n\nEl barrio con el nombre mas largo es {} y el que presenta el nombre mas corto es {} ".format(mayor_nombre, minimo_nombre))

consumo_mayor = max(diccionario["Agua"].values())
consumo_menor = min(diccionario["Agua"].values())

print("\n\nEl mayor consumo de agua es: {}".format(consumo_mayor))
print("El menor consumo de agua es: {}".format(consumo_menor))

consumo_mayor = max(diccionario["Gas"].values())
consumo_menor = min(diccionario["Gas"].values())

print("\n\nEl mayor consumo de Gas es: {}".format(consumo_mayor))
print("El menor consumo de Gas es: {}".format(consumo_menor))

consumo_mayor = max(diccionario["Internet"].values())
consumo_menor = min(diccionario["Internet"].values())

print("\n\nEl mayor consumo de internet es: {}".format(consumo_mayor))
print("El menor consumo de internet es: {}".format(consumo_menor))

consumo_mayor = max(diccionario["Energía"].values())
consumo_menor = min(diccionario["Energía"].values())

print("\n\nEl mayor consumo de energia es: {}".format(consumo_mayor))
print("El menor consumo de energia es: {}".format(consumo_menor))

maximo_habitantes = max (diccionario["Habitantes"].values())
minimo_habitantes = min (diccionario["Habitantes"].values())

print("\nLa cantidad maxima de habitantes es {} y la cantidad minima es {} ".format(maximo_habitantes, minimo_habitantes))