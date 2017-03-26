passwdAdmin = "navas"

# Objeto decorador

def admin(decorar):
	def validar(*args,**kwargs):
		if loggeado:
			decorar(*args,**kwargs)

		else:
			print "No tiene permiso para usar la funcion", decorar.__name__

	return validar

# Funcion decorada

@admin
def suma():
	a = input("Numero 1: ")
	b = input("Numero 2: ")

	print "\nResultado:", a + b


passwd = raw_input("Password: ")

if passwd == passwdAdmin:
	loggeado = True

else:
	loggeado = False


# Llamada de la funcion decorada
suma()






