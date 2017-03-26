lista = []

n = raw_input("Nombre: ")

n2 = raw_input("Nombre: ")

lista.append(n + "&" + n2)

for elemento in lista:
	mostrar = elemento.split("&") # El metodo split permite separar una cadena por cada
								  # separador que consiga y convertirlo en una lista

if mostrar.count(n) == 2:    # El metodo count devuelve un entero con la cantidad de veces
							 # que aparece un elemento en la lista
	print ("\nEl segundo Nombre es igual que el primero")
	print mostrar

else:
	print ("\nLos nombres son diferentes")
	print mostrar
