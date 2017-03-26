#encoding: utf-8 				# CODIFICACION PARA USAR LA LETRA "ñ"

# Condicionales
# Para declarar un condicional se coloca la condicion sin parentesis
# y al final de la condision se coloca dos puntos ":".

print 
edad = raw_input("Intruduce tu edad: ")
edad = int (edad)

if edad >= 0 and edad < 18:
	print
	print "[Eres un niño]"
elif edad >= 18 and edad < 27:
	print
	print "[Eres un joven]"
elif edad >= 27 and edad < 60:
	print
	print "[Eres un adulto]"
else:
	print
	print "[Eres de la tercera edad]"