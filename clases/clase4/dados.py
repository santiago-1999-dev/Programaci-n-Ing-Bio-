import random 
#-------MENSAJES--------
MENSAJE_FALLA = "Fallaste, no has sacado 12"
MENSAJE_ACIERTO = "Acertaste, felicitaciones sacaste 12"
MENSAJE_OPORTUNIDAD = "Vuelave a lanzar los dados"
#-----VARIABLES----------
NUMERO_ESPERADO = 12
suma = 2
dado1 = 0
dado2 = 0
#-------CODIGO-----------
while (suma != NUMERO_ESPERADO):
    print (MENSAJE_FALLA) 
    print (MENSAJE_OPORTUNIDAD)
    dado1 = random.randint (1,6)
    dado2 = random.randint (1,6)
    suma = dado1 + dado2
    print ( dado2 , dado1)
print (MENSAJE_ACIERTO)