#--------MENSAJES-------
MENSAJE__BIENVENIDO ="Bienvenido a la clinica"

#-----------CODIGO----------------


print (MENSAJE__BIENVENIDO)


_decision = int (input("""
    ingrese :
    1- para ver lista de doctores, enfermeros y pacientes
    2- para crear una lista de personas 
    3- para ver el estado de los pacientes
    4- salir
"""))
while (_decision != 4):
    if (_decision == 1):
        def mostrar_tres_listas ( lista_1 , lista_2 , lista_3):
            if ( len ( lista_1 ) ==  len ( lista_2 ) == len (lista_3)):
                print ("doctores -" , "enfermeros -" , "pacientes")
                for i  in range ( len ( lista_1 )):
                    print ( lista_1 [ i ] , lista_2 [ i ] , lista_3 [i])

            
    

        doctores = ["Santiago --", "Daniel --", "Valeria --", "Fernanda --", "Camila --"]
        enfermeros = ["Juanes --", "Marco --", "Elena --", "Daniel --", "Ysabella --"]
        pacientes = ["Andrea", "Camila", "Ramiro", "Esteban", "Juan"]   

        mostrar_tres_listas (doctores , enfermeros , pacientes)

    elif (_decision == 2):
        def llenarlista ():
            lista = []
            decision = input ("inngrese s--> para agregar mas personas n--> para no agregar mas personas : ")
            while (decision == "s"):
                lista.append (input("Ingrese una persona a la lista : "))
                decision = input ("inngrese s--> para agregar mas personas n--> para no agregar mas personas : ")
            return lista 
        print ("ingrese la lista de doctores : ")
        doctores = llenarlista ()
        print ("ingrese la lista de enfermeros : ")
        enfermeros = llenarlista ()
        print ("ingrese la lista de pacientes : ")
        pacientes = llenarlista ()
        
        mostrar_tres_listas (doctores, enfermeros, pacientes)

    elif (_decision == 3):
        def mostrar_dos_listas ( lista_1 , lista_2):
            if ( len ( lista_1 ) ==  len ( lista_2 )):
                print ("pacientes -" , "estado")
                for i  in range ( len ( lista_1 )):
                    print ( lista_1 [ i ] , lista_2 [ i ])

        pacientes = ["Andrea --", "Camila --", "Ramiro --", "Esteban --", "Juan --"] 
        estado = ["grave", "estable", "UCI", "estable", "grave"]

        mostrar_dos_listas (pacientes, estado)

    else:
        print("ingrese un valor valido")

    _decision = int (input("""
      ingrese :
        1- para ver lista de doctores, enfermeros y pacientes
        2- para crear una lista de personas 
        3- para ver el estado de los pacientes
        4- salir
    """))
print("gracias por usar el programa")

    

