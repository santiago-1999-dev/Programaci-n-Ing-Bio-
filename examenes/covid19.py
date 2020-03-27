#--------MENSAJES-------
MENSAJE__BIENVENIDO ="Bienvenido a la clinica"
presion = 0.0
#-----------CODIGO----------------
print (MENSAJE__BIENVENIDO)

_decision = int (input("""
    ingrese :
    1- para mostrar en pantalla el peso y el valor de la presion calculada
    2- para añadir peso de pacientes 
    3- para ver informacion de las presiones
    4- salir
"""))
while (_decision != 4):
    if (_decision == 1):
        def mostrar_dos_listas ( lista_1 , lista_2):
            if ( len ( lista_1 ) ==  len ( lista_2 )):
                print ("peso -" , "presion -")
                for i  in range ( len ( lista_1 )):
                    print ( lista_1 [ i ] , lista_2 [ i ])

        pesosPacientes = [32,64,74,85,98,115,122,127,137,148]

        presiones=[]
        for peso in pesosPacientes:
            presiones.append(peso*6)
        print(presiones)



        mostrar_dos_listas (pesosPacientes, presiones)


    elif (_decision == 2):
        def mostrar_lista (lista_1):
            if ( len ( lista_1 )):
                print ("Esta es la lista de los pesos nuevas ingresados")
                for i  in range ( len ( lista_1 )):
                    print (lista_1[i])

        def llenarlista ():
            lista = []
            decision = input ("ingrese s--> para agregar mas pesos n--> para no agregar mas pesos : ")
            while (decision == "s"):
                lista.append (input("Ingrese el peso del paciente a la lista : "))
                decision = input ("ingrese s--> para agregar mas pesos n--> para no agregar mas pesos : ")
            return lista 

        print ("desea inngresar el peso de los pacientes? : ")
        pesos = llenarlista ()

        mostrar_lista (pesos)
        

    elif (_decision == 3):
        print ("la presion mas alta en la lista de nuevos {} es el {}"
        .format(presiones, max (presiones)))
        print ("la presion mas baja en la lista de los nuevos {} es el {}"
        .format(presiones, min (presiones)))
        presiones.sort(reverse=True)
        print ("lista de presiones en orden decreciente {}".format(presiones))
        print ("esta es la cantidad de pacientes ingresados")
        print (len(pesosPacientes))
        print (len(pesos))
               
    else:
        print("ingrese un valor valido")
        
        
    _decision = int (input("""
     ingrese :
        1- para mostrar en pantalla el peso y el valor de la presion calculada
        2- para añadir peso de pacientes 
        3- para ver informacion de las presiones
        4- salir
    """))

print ("gracias por utilizar el programa")