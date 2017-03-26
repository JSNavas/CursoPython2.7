# Las funciones de orden superior son las que son retornada
# por otra funcion, existen 2 formas de retornar un funcion:

# retornando una funcion ejecutada, es decir, se ejecuta la 
# funcion y lo que se retorna es el valor que retorna esa
# funcion

# retornando una funcion sin ejecutar, es decir, que se trata
# a la funcion como si fuera cualquier variable y no se ejecuta
# hasta el momento que llamemos la funcion que retorna esa funcion

def saludo(persona):
	print "hola",persona

def imprimir(funcion):
	return funcion 		# Retorno de una funcion sin ser ejecutada

persona = "navas"

imprimir(saludo(persona))

#####################################################################

def saludo(persona):
	print "hola",persona

def imprimir(funcion):
	return funcion(persona) # Retorno de una funcion ejecutada que
							# recibe parametros

imprimir(saludo)

#####################################################################

def saludo():
	print "hola"

def imprimir(funcion):
	return funcion() 		# Retorno de una funcion ejecutada que
							# no recibe ningun parametro

imprimir(saludo)

