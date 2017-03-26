# Funcion a utilizar con map()y reduce()

def suma(a, b):
	return a + b # retorna una suma o concatenacion


# Funcion a utilizar con filter()

def filtrar(n):
	return (n > 5) # retorna si los numeros son mayores a 5
	

l1 = [1,5,4,3,8,6,3,9,6]
l2 = [1,2,3,4,5,6,7,8,9]

# La funcion lambda es una funcion que sustituye
# a las demas funciones para solo ser llamada cuando
# se necesite y despues deja de existir en el programa

print "Sin la funcion lambda: "
print map(suma,l1,l2)
print filter(filtrar,l1)
print reduce(suma,l2)

print"\nCon la funcion lambda: "
print map(lambda a,b: a+b, l1,l2) 
print filter(lambda n: n>5,l1)
print reduce(lambda a,b: a+b,l2)

