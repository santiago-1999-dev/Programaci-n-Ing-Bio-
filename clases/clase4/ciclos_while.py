# numero = 0
# NUMERO_DESEADO = 12
# while (numero <= NUMERO_DESEADO):
#     numero = numero +1
#     print (numero)
# print (numero)

import random 
PREGUNTA_NUMERO = """Ingrese un numero 
entero 
entre 1 - 10 
:"""
MENSAJE_FALLO = "Fallaste!!! intentalo de nuevo"
MENSAJE_ACIERTO = "Felicidades sabes mi numero favorito"
MENSAJE_MAYOR = "estas cerca el numero que ingresaste es mas grande"
MENSAJE_MENOR = "estas cerca el numero que ingresaste es mas menor"
numero = 0
NUMERO_FAVORITO = random.randint(1,10)
_numeroIngresado = int (input (PREGUNTA_NUMERO))
while (_numeroIngresado != NUMERO_FAVORITO):
    print (MENSAJE_FALLO)
    if (_numeroIngresado > NUMERO_FAVORITO): print (MENSAJE_MAYOR)
    else: print (MENSAJE_MENOR)
    _numeroIngresado = int (input (PREGUNTA_NUMERO))
print(MENSAJE_ACIERTO)