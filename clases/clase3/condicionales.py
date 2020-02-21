#-------------Mensajes---------------- 
MENSAJE__BIENVENIDO ="Bienvenido"
MENSAJE_ENTRADA ="a este programa"
MENSAJE_EDAD ="Tu edad es"
MENSAJE_ESTATURA ="Tu estatura es"
MENSAJE_TOCAYO = "Hola hermano somos tocayos"
PREGUNTA_NOMBRE = "ingrese su nombre : \n"
MENSAJE_DESPEDIDA = "CHAO"
PREGUNTA_EDAD = "ingrese por favor su edad : \n"
MENSAJE_JOVEN = "Eres joven"
MENSAJE_ADULTO = " Eres adulto"
MENSAJE_VIEJO = "Eres viejo"
#------------VARIABLES--------------
NOMBRE_PERSONAL = "Santiago"
#-------------ENTRADAS------------------
_nombreUsuario = " "
_edadUsuario = 0
#-------------CODIGO-------------------
print(MENSAJE__BIENVENIDO)
_nombreUsuario = input (PREGUNTA_NOMBRE)
if(NOMBRE_PERSONAL == _nombreUsuario) :
    print(MENSAJE_TOCAYO)
print(MENSAJE_DESPEDIDA)
_edadUsuario = int (input(PREGUNTA_EDAD))

if ((_edadUsuario >= 0) and (_edadUsuario <= 25)) :
    print(MENSAJE_JOVEN)
elif((_edadUsuario >= 26) and (_edadUsuario <= 65)):
    print(MENSAJE_ADULTO)
else:
     print(MENSAJE_VIEJO)
print(MENSAJE_DESPEDIDA)











