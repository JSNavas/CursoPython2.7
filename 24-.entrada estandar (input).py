lista = []

n = input("\nCuantos numeros desea agregar a la lista: ")

# La entrada input lee el tipo
# de dato del valor que se ingrese,
# ejemplo si es un entero, lo lee como entero.

# La funcion input solo funciona con numeros
# ya que si se agrega un string se tendria
# que ingresar como string con las comillas
# "String"

print
i = 0

while i < n:
    lista.append(input("valor %d: " % (i + 1)))
    i += 1

print

for recorrer in lista:
    print recorrer
