#--------MENSAJES-------
MENSAJE__BIENVENIDO ="Bienvenido"

#-------CODIGO------------
PREGUNTA_EDAD = "Ingrese su edad : "
#-------CODIGO------------
PREGENTA_LISTA_COMPRAS = "Desea comprar productos ? s ->si n->no : "
#-------CODIGO------------
listaCompras = "Esta es su lista de compras elemento a elemento : "
#-------CODIGO------------
eliminarCompras = "Deseas eliminar un elemento de la lista ? cual ? s ->si n->no : "
#------CODIGO----------
PREGUNTA_NUMERO = "Ingrese el numero del elemento que quiere eliminar : "
#------------------------
print(MENSAJE__BIENVENIDO)


_decision = int (input("""
    ingrese :
    1- Edad 
    2- Lista de productos que desea comprar
    3- Lista de compras elemento a elemento 
    4- Eliminar uno de los elementos de la lista de compras 
    5- Salir 
"""))


while (_decision != 5):
    if (_decision == 1):
        _edadUsuario = int (input(PREGUNTA_EDAD))
        if ((_edadUsuario >= 0) and (_edadUsuario <= 17)) :
                print("no puedes ingresar")
        elif((_edadUsuario >= 18) and (_edadUsuario <= 29)):
                print("puedes ingresar")
        elif((_edadUsuario >=30) and (_edadUsuario <=59)):
                print("tienes descuento del 30%")
        else:
            print("tienes descuento igual a tu edad")

    elif (_decision == 2):
        productos = []
        _listaCompra = input (PREGENTA_LISTA_COMPRAS)
        while (_listaCompra == "s" ) :
            productos.append (input ("ingrese : "))
            _listaCompra = input (PREGENTA_LISTA_COMPRAS)
        print (productos)
        
    elif (_decision == 3):
        print(listaCompras)
        print(productos)

    elif (_decision == 4):
        print (productos)
        _numeroIngresado = int (input(PREGUNTA_NUMERO))
        productos.pop (_numeroIngresado)
        print (productos)
            
           
            
    else:
        print("ingrese un valor valido")
    _decision = int (input("""
      ingrese :
        1- Edad 
        2- Lista de productos que desea comprar
        3- Lista de compras elemento a elemento 
        4- Eliminar uno de los elementos de la lista de compras 
        5- Salir 
    """))
print ("gracias por usar el programa")

    




