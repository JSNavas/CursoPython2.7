n = int(raw_input("\nCuantos nombres desea ingresar: ")) # Se convierte en entero con la funcion "int"
														 # antes del raw_input, para que el raw_input
														 # este dentro de los parentesis del int y asi	
														 # el numero que ingrese el usuario no sera
lista = [] # Se declara una lista vacia				     # interpretado como un string.

i = 0

print

while i < n:
	lista.append(raw_input("Nombre %d: " % (i+1)))  # Se rellena la lista, colocando el nombre de la 
	i = i + 1									    # lista luego usando la funcion ".append" seguidos
													# de dos parentesis "lista.append()" dentro de los
													# parentesis estaria el raw_input para que se leea
													# los valores que va ingresando el usuario y se
													# vayan anexando a la lista.

print "\nLos 3 nombres son: \n"

for recorrer in lista:
	print recorrer