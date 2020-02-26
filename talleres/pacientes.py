#------------MENSAJES----------------------#
MENSAJE__BIENVENIDO ="Bienvenido"
MENSAJE_DESPEDIDA = "CHAO"
PREGUNTA_PACIENTES = "Ingrese numero de pacientes : \n"
MENSAJE_RIESGO_MEDIO = "Estan en riesgo medio"
MENSAJE_RIEGO_BAJO = "Estan en riesgo bajo"
MENSAJE_RIEGO_ALTO = "Estan en riesgo alto"
MENSAJE_UCI = "Estan en alto riesgo"
PREGUNTA_UCI = "Ingrese numero de pacientes en uci : \n"


#------------VARIABLES---------------------#
NOMBRE_PERSONAL = "Santiago"


#------------ENTRADAS-----------------------#
_numeroPacientes= 0
_numeroPacientesuci = 0
#-------------CODIGO------------------------#
print(MENSAJE__BIENVENIDO)
_numeroPacientes = int (input (PREGUNTA_PACIENTES))
if ((_numeroPacientes >= 0) and (_numeroPacientes <= 1000)):
    print (MENSAJE_RIEGO_BAJO)
elif ((_numeroPacientes >1000) and (_numeroPacientes <= 5000)):
    _numeroPacientesuci = int (input (PREGUNTA_UCI))
    print (MENSAJE_RIESGO_MEDIO)
    if ((_numeroPacientesuci >= 1000)):
        print (MENSAJE_UCI)
    else: 
        print (MENSAJE_RIESGO_MEDIO)
else:
     print(MENSAJE_RIEGO_ALTO)
print (MENSAJE_DESPEDIDA)



