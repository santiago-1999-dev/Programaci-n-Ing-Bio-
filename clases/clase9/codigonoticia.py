import funciones_noticias as helper 
##Leimos el archivo
lineas = helper.leer_archivo ("noticias.txt")
#Lo mostramos linea por linea
helper.mostrar_lineas(lineas)

Texto = ["Hola a todos esta es mi opinion frente al desencanto:\n"
"Las relaciones interpersonales son de gran importancia para nuestro desarrollo,\n"
"como seres humanos tenemos una carencia eterna y profunda de ser amados,\n"
"en el momento que esto no sucede nuestra existencia pierde sentido,\n"
"por ello debemos tener un amor mas grande que nosotros y ese es el amor de Dios."]
helper.escritura_archivo ("Opinion.txt",Texto)
helper.agregar_lineas_archivo("noticias.txt","\nGabriel garcia Marquez\n16 de Abril")



