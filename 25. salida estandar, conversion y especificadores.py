# CONVERSION

# Todo valor ingresado por teclado se va leer como un string
# por lo que hay que convertirlo al tipo que queramos que sea

# ESPECIFICADORES

# Los especificadores permiten convertir una variable al tipo
# que queramos %d convierte a entero, %f convierte a flotante,
# %s convierte a string, %h a hexadesimal y %o a octal.

try:
	edad = raw_input("Intruduce tu edad: ")	# ENTRADA ESTANDAR PARA LEER POR TECLADO Y GUARDAR EL VALOR EN "edad".
	edad = int (edad)						# CONVERSION A ENTERO
except:
	print "El valor es incorrecto."			# CONDICION EN EL CASO DE QUE NO SE CUMPLA LA CONDICION Y LA EDAD NO SEA UN ENTERO.

else:										# SI SE CUMPLE LA CONDICION
	print "Tu edad es: %d entonces eres %.8s, %.2f" % (edad, "mayor de edad",edad)
																				 # ".2" PARA QUE MUESTRE 2 NUMEROS MAS, DESPUES DE LA COMA (SE PUEDE USAR CON CUALQUIER ESPECIFICADOR).
																				 # ".8" PARA QUE SOLO MUESTRE 8 ESPACIOS DEL STRING
																				 # USO DE ESPECIFICADORES
																				 # Y SALIDA ESTANDAR PARA
																				 # MOSTRAR POR PANTALLA
	print
	print "%20s?" % ("Esa es tu edad")									# 20 PARA QUE MUESTRE 20 ESPACIOS A LA IZQUIERDA
	print "%-20s?" % ("Esa es tu edad")									# -20 PARA QUE MUESTRE 20 ESPACIOS A LA DERECHA


