lista = []

def Datos():
	print "Introduzca 3 numeros enteros: "
	i = 0
	
	while i < 3:
		lista.append(input())
		i += 1


def Mostrar():
	print "\nNumeros ingresados: \n"

	for elemento in lista:
		print elemento