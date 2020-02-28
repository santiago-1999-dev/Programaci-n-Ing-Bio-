#------------MENSAJES----------------------#
MENSAJE__BIENVENIDO ="Bienvenido"
MENSAJE_DESPEDIDA = "Que te mejores"
MENSAJE_SALUDABLE = "Estas saludable"
MENSAJE_HIPOTERMIA = " Estas en hipotermia"
MENSAJE_ALERTA = "Estas en alerta"
MENSAJE_PELIGRO = "Estas en peligro"
MENSAJE_OBSERVACION = "Estas en observacion"
PREGUNTA_PAIS = "Ingrese su pais de procedencia : \n"
PREGUNTA_TEMPERATURA = "Ingrese la temperatura del paciente : \n"
#------------VARIABLES---------------------#
NOMBRE_PERSONAL = "Santiago"

#------------ENTRADAS-----------------------#
_paisPaciente = "  "
_temperaturaPaciente = 0.0


#-------------CODIGO------------------------#
print(MENSAJE__BIENVENIDO)
_paisPaciente = input (PREGUNTA_PAIS)
if (_paisPaciente == "China") or (_paisPaciente == "Iran") or (_paisPaciente == "Italia"):
    print (MENSAJE_OBSERVACION)
else:
    _temperaturaPaciente = float (input (PREGUNTA_TEMPERATURA))
    if ((_temperaturaPaciente >= 36) and (_temperaturaPaciente <= 38.4)):
        _temperaturaPaciente = float (input (PREGUNTA_TEMPERATURA))
        print (MENSAJE_SALUDABLE)
    elif ((_temperaturaPaciente >= 36) and (_temperaturaPaciente <= 38.5)):
            print (MENSAJE_HIPOTERMIA)
    elif ((_temperaturaPaciente >= 38.5) and (_temperaturaPaciente <= 40)):
            print (MENSAJE_ALERTA)
    else: 
        print (MENSAJE_PELIGRO)
print (MENSAJE_DESPEDIDA)
    


   






