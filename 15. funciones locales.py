# Para declarar una funcion local se utiliza la palabra reservada"def"
# luego el nombre de la funcion, entre parentesis "()" losdatos que se
# le van a pasar a la funcion y para cerrar la declaracion ":".

# Declaracion de la funcion local pasandole un parametro
def saludo(elnombre):
	print "Bienvenido",elnombre
	
nombre = raw_input("\nIngrese su nombre: ")
saludo(nombre)				# El llamado de la funcion se hace sin los ":"