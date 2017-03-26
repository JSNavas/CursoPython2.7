lista = ["bienvenido "]

ciclo = (c * 4 for c in lista)


print ciclo

print ciclo.next()

for cadena in ciclo:
	print cadena

print
n = input("Factorial de: ")

def factorial(n):
	i = 1
	while n > 1:
		i = n * i
		yield i
		n -= 1

for fact in factorial(n):
	print fact







