# lista_mercado [0] = " salchicha"    para cambiar
# lista_mercado.append("huevo")       para agregar 
# lista_mercado.pop(0)                numero que quiero cambiar
# print (len(lista_mercado))          numero de elementos


#---------CODIGO---------
listaNombres = ["Santiago" ,
"Daniel" , 
"Fernanda" ,
"Elena" , 
"Juanes" , 
"Ysabella" , 
"David" , 
"Maria Camilas",
"Marco"] 
listaNombres [4] = "Ysabella"
listaNombres [5] = "Esteban"
listaNombres.pop(-2)
listaNombres.append("Maria Camila")
print (listaNombres)

#---------------------------
listaEdades = [18 , 
19 , 
20 , 
18 , 
17 , 
18 , 
21 , 
25 , 
24 ]
print (listaEdades)
#-------------------------
listaNotas = [4.4 , 
4.5 , 
4.6 , 
5.0 , 
3.6 , 
3.9 , 
2.9 , 
5.0 ,
4.9 ]
print (listaNotas)
#--------CODIGO------------
_decision = int (input("""
    ingrese :
    1- para ver lista de nombre
    2- para ver edades
    3- para ver notas
    4- salir
"""))
while (_decision != 4):
    if (_decision == 1):
        print(listaNombres)
    elif (_decision == 2):
        print(listaEdades)
    elif (_decision == 3):
        print(listaNotas)
    else:
        print("ingrese un valor valido")
    _decision = int (input("""
     ingrese :
        1- para ver lista de nombre
        2- para ver edades
        3- para ver notas
        4- salir
    """))




    
    
        


    



        


