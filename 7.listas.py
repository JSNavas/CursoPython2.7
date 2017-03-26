# Listas = arreglos o vectores

# Acceder a listas dentro de otra lista

# Se accede a traves del indice de donde se  encuentra la lista
# que esta dentro de la lista principal y al lado se coloca el 
# indice al que queramos acceder de la lista que esta adentro. 
# En este caso la lista que esta adentro se encuentra en el 
# indice [5] y el indice al que quiero acceder de esa lista
# es el numero [1]

lista = [1,2,3,4,5,[6,7,8,9]]
acceso = lista[5][1]

# Si solo se quiere mostrar lo que contiene la lista de adentro
# se coloca solo el indice en donde se encuentra la lista

acceso2 = lista[5]

print "LISTA CON UNA LISTA ADENTRO"
print "lista principal"
print lista
print " 0  1  2  3  4 5[0  1  2  3]  <- INDICE DE LA LISTA\n"
print acceso
print
print "Lista de adentro"
print acceso2

# Para acceder directamente a las lista de forma inversa se utiliza
# los indice -1,-2,-3 etc... Comenzando por el 1, es decir, si
# si queremos acceder al ultimo numero de un arreglo, se coloca el -1

#en este caso mostraria la lista que esta adentro, ya que la lista es la ultima

print
print "ACCEDER DE FORMA INVERSA AL ULTIMO ELEMENTO DE LA LISTA"
acceso3 = lista[-1]
print acceso3

# Si se quiere acceder al ultimo elemento de la lista que esta adentro

print
print """ACCEDER AL ULTIMO ELEMENTO DE LA LISTA QUE SE ENCUENTRA DENTRO DE LA 
LISTA PRINCIPAL"""
acceso4 = lista[-1][-1]
print
print acceso4