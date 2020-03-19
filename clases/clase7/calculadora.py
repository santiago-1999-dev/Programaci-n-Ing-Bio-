def sumar (x,y):
    suma = x+y 
    return suma

def restar (x,y):
    resta = x-y
    return resta

def dividir (x,y):
    division = 0
    if y == 0 :
        division = "operacion no valida"
    else:
        division = x/y
    return division 

def multiplicar (x,y):
    multiplicacion = x*y
    return multiplicacion

print (sumar(3,7))
print (restar(8,5))
print (dividir (6,2))
print (multiplicar(5,2))

