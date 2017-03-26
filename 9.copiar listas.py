# Copiar listas 

lista = [1,2,3,4,5,6,7,8,9]

# Se especifica (desde que indice va a empezar : hasta cuantos elementos de "lista" va a copiar) 
lista2 = lista[0:5] 

print "COPIAR LISTAS\n"
print "LISTA"
print lista
print
print " 0  1  2  3  4  5  6  7  8   <- INDICE DE LA LISTA"
print " 1  2  3  4  5  6  7  8  9 <- Elementos que contiene (lista)\n"
print lista2
print

# Si se quiere copiar uno si y uno no, se agrega otros : y se coloca la longitud del salto +1
# en este caso la longitud es de uno en uno, + 1 seria 2.
print "COPIAR LISTA UNO SI, UNO NO"
lista3 = lista[0::2] # O tambien lista3 = lista[0:9:2]
print
print lista3