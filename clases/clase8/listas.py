#--------MENSAJES-------
MENSAJE__BIENVENIDO ="Bienvenido al programa"
promedio = 0.0
#-----------CODIGO----------------


print (MENSAJE__BIENVENIDO)

def mostrar_lista (lista_1):
    if ( len ( lista_1 )):
        print ("Esta es la lista de edades nuevas ingresadas")
        for i  in range ( len ( lista_1 )):
            print (lista_1[i])

def llenarlista ():
    lista = []
    decision = input ("ingrese s--> para agregar mas edades n--> para no agregar mas edades : ")
    while (decision == "s"):
        lista.append (input("Ingrese la edad del paciente a la lista : "))
        decision = input ("ingrese s--> para agregar mas personas n--> para no agregar mas personas : ")
    return lista 

print ("desea inngresar la edad de los pacientes? : ")
edades = llenarlista ()

mostrar_lista (edades)


promedio = (((1+2+4+8+16+32+64)/7))
print ("este es el promedio de edad : ")
print (promedio)


lista_Edades_Iniciales = [1,2,4,8,16,32,64]
lista_adicionar = [edades]
lista_adicionar.extend(lista_Edades_Iniciales)
print (lista_adicionar)


print ("la edad mas grande en la lista de nuevos {} es el {}"
.format(edades, max (edades)))
print ("la edad mas grande en la lista inicial {} es el {}"
.format(lista_Edades_Iniciales, max(lista_Edades_Iniciales)))


print ("la edad mas pequeña en la lista de los nuevos {} es el {}"
.format(edades, min (edades)))
print ("la edad mas pequeña en la lista inicial {} es el {}"
.format(lista_Edades_Iniciales, min (lista_Edades_Iniciales)))

edades.sort()
print ("lista nuevos ordenada creciente {}".format(edades))
lista_Edades_Iniciales.sort()
print ("lista iniciales ordenada creciente {}".format(lista_Edades_Iniciales))

edades.sort(reverse=True)
print ("lista nuevos ordenada decreciente {}".format(edades))
lista_Edades_Iniciales.sort(reverse=True)
print ("lista iniciales ordenada decreciente {}".format(lista_Edades_Iniciales))


lista_Edades_Iniciales.insert (4,87)
print("usted a insertado el numero 87 en la pocision 4")
print (lista_Edades_Iniciales)

valor_eliminado = lista_Edades_Iniciales.pop(6)
print (lista_Edades_Iniciales, 
"la edad elimina fue el numero {} de la pocision seis de la lista"
.format(valor_eliminado))














