# Bucles

# Uso del bucle while:
# En bucle while se incializa el valor que estara dentro del bucle
# luego se declara la condicion seguido de los ":"
# y siguiendo la identacion mostrar los valores y luego
# el incremento que se realiza sumandole + 1 al valor del bucle


# Mostrar los numeros del 0 al 20
n = 0

print "Numeros del 0 al 10: "
print

while n <= 10:
	print n
	n += 1 

print

# Uso de la palabla reservada "break"

n2 = 1

# Bucle while con condicionales

print "Numeros del 1 al 30: "
print

while n2 <= 30:
	if n2 == 21:
		break				# El break finaliza el ciclo al momento de que se cumpla la condicion por lo que no es necesario que se incremente
	print n2
	n2 = n2 + 1 

# Uso de la palabla reservada "continue"

n3 = 1

print
print "Numeros del 1 al 30: "
print

while n3 <= 30:
	if n3 == 21:
		n3 = n3 + 1
		continue			# El continue evita que se imprima lo que sigue despues del continue

	print n3
	n3 = n3 + 1