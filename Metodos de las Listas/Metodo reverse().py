cadena = raw_input('Escribe una palabra para invertir: ')

lista = list(cadena)
lista.reverse()

cadenaInversa = "".join(lista) 

print 'Cadena al reves:',cadenaInversa
