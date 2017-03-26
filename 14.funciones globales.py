# Para declarar una funcion global se utiliza la palabra reservada
# "def" luego el nombre de la funcion seguido de 2 parentesis "()"
# y para cerrar la declaracion ":"

# Declaracion de una funcion vacia
def pedir_ndad():
	pass 		# El pass se utiliza para decirle a python que todavia no vas a utilizar la funcion
				# si no, reconoceria la funcion como un error ya que las funciones tienen que tener
				# algo dentro de ellas.

# Declaracion de la funcion global
def pedir_nombres():
	nombre = raw_input("\nIngrese su nombre: ")
	print "\nBIENVENIDO,",nombre


# llamado de la funcion
pedir_nombres()