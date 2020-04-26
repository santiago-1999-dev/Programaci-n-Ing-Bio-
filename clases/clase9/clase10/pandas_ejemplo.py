import pandas as p
diccionario =p.read_csv("balance.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict()
print(diccionario)
print(diccionario.keys())
print(diccionario["Ciudad"])


mayor_nombre = max (diccionario["Ciudad"].values(), key=len)
minimo_nombre = min (diccionario["Ciudad"].values(), key=len)

print("\n\nla Ciudad con el nombre mas largo es {} y la que presenta el nombre mas corto es {} ".format(mayor_nombre, minimo_nombre))

ganancia_mayor = max(diccionario["Ganancias"].values())
mayor_perdida = max(diccionario["Perdidas"].values())

print("\n\nla mayor ganancia fue {}".format(ganancia_mayor))
print("\n\nla mayor perdida fue {}".format(mayor_perdida))
