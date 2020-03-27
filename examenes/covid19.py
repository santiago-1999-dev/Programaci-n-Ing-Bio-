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

        peso_1 = 32
        presion_1 = (6*peso_1)
        peso_2 = 64 
        presion_2 = (6*peso_2)
        peso_3 = 74
        presion_3 = (6*peso_3)
        peso_4 = 85
        presion_4 = (6*peso_4)
        peso_5 = 98
        presion_5 = (6*peso_5)
        peso_6 = 115
        presion_6 = (6*peso_6)
        peso_7 = 122
        presion_7 = (6*peso_7)
        peso_8 = 127
        presion_8 = (6*peso_8)
        peso_9 = 137
        presion_9 = (6*peso_9)
        peso_0 = 148
        presion_0 = (6*peso_0)

        print (presion_1,presion_2,presion_3,presion_4,presion_5,presion_6,presion_7,presion_8,presion_9,presion_0)
       
        pesosPacientes = [32,64,74,85,98,115,122,127,137,148]
        presionesPacientes = [presion_1, presion_2, presion_3,presion_4,presion_5,presion_6,presion_7,presion_8,presion_9,presion_0 ]


        mostrar_dos_listas (pesosPacientes, presionesPacientes)


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
        .format(presionesPacientes, max (presionesPacientes)))
        print ("la presion mas baja en la lista de los nuevos {} es el {}"
        .format(presionesPacientes, min (presionesPacientes)))
        presionesPacientes.sort(reverse=True)
        print ("lista de presiones en orden decreciente {}".format(presionesPacientes))
        print ("esta es la cantidad de pacientes ingresados")
        print (len(pesosPacientes))
               
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