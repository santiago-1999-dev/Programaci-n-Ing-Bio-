#------------MENSAJES----------------------#
MENSAJE__BIENVENIDO ="Bienvenido"
MENSAJE_DESPEDIDA = "CHAO"
PREGUNTA_NOMBRE = "ingrese su nombre : \n"
PREGUNTA_PESO = "ingrese su peso : \n"
PREGUNTA_ESTATURA = " ingrese su estatura \n"
MESAJE_PESO_BAJO = "estas bajo de peso"
MENSAJE_PESO_SALUDABLE = "estas saludable"
MESAJE_SOBREPESO = "estas en sobrepeso"
MESAJE_OBESIDAD_MORBIDA = "estas en obesidad morbida"
MESAJE_TOCAYO = "Somos tocayos morbidos"
#------------VARIABLES---------------------#
NOMBRE_PERSONAL = "Santiago"
IMC = 0.0
#------------ENTRADAS-----------------------#
_nombreUsuario = " "
_pesoUsuario = 0.0
_estaturaUsuario = 0.0

#-------------CODIGO------------------------#
print(MENSAJE__BIENVENIDO)
_nombreUsuario = input (PREGUNTA_NOMBRE)
_pesoUsuario = float (input(PREGUNTA_PESO))
_estaturaUsuario = float (input(PREGUNTA_ESTATURA))
IMC = ((_pesoUsuario/_estaturaUsuario**2))
print (IMC)
if ((IMC >= 12) and (IMC<=18)):
    print(MESAJE_PESO_BAJO)
elif((IMC >=19) and (IMC <=24)):
    print(MENSAJE_PESO_SALUDABLE)
elif((IMC >=30) and (IMC <=39)):
    print(MESAJE_SOBREPESO)
else:
    print(MESAJE_OBESIDAD_MORBIDA)
    print(MESAJE_TOCAYO)

print(MENSAJE_DESPEDIDA)
