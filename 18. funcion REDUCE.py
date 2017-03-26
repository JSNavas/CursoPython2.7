lista = ["hola", "como", "estas"]

def concatenar(a, b):
	return a + " " + b

concatenado = reduce(concatenar,lista)

print type(concatenado)
print concatenado