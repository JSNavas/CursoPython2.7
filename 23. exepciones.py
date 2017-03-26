try:
	edad = raw_input("Intruduce tu edad: ")
	edad = int (edad)
except:
	print "El valor es incorrecto."

finally:
	print "Esto se ejecuta siempre"

else:
	print "Tu edad es: %d" % (edad)

