
#Mensajes 
MENSAJE__BIENVENIDO="Bienvenido"
MENSAJE_ENTRADA ="a este programa"
MENSAJE_EDAD="Tu edad es"
MENSAJE_ESTATURA="Tu estatura es"
#Preguntas
PREGUNTA_NOMBRE="ingrese su nombre : "
PREGUNTA_EDAD="ingrese su edad : "
PREGUNTA_ESTATURA="ingrese su estatura : "


_nombrePersona = input(PREGUNTA_NOMBRE)
print(MENSAJE_BIENVENIDO,_nombrePersona, MENSAJE_ENTRADA)
_edadPersona = input(PREGUNTA_EDAD)
print(MENSAJE_EDAD,_edadPersona)
_estaturaPersona = input(PREGUNTA_ESTATURA)
print(MENSAJE_ESTATURA,_estaturaPersona)
print (type(_estaturaPersona))
