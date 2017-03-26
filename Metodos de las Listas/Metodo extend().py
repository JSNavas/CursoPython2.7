lista = [1,2,3,4,5]

lista2 = [6,7,8,9,10]

print "\nlista 1: "
print lista

print "\nlista 2: "
print lista2

lista.extend(lista2) # El metodo extend te permite agregar los elementos de un lista
					 # al final de la lista en la que se utilice este metodo

print "\nLista extendida: "
print lista