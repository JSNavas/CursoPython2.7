# Cambiar valores de una lista

lista = [1,2,3,4,5,6,7,8,9]

# Para cambiar un solo valor de la lista se coloca el indice del valor que queramos cambiar

lista [6] = 56

# Para cambiar  2 valores de una lista, es obligatorio meter esos nuevos valores en una lista.
# sin olvidar que se especifica (desde que indice va a empezar : hasta cuantos elementos de "lista"
# va a cambiar) 

lista[0:2] = [24,65]

# Para reemplazar 2 numeros por un numero, se lo coloca de igual manera para cambiar 2 valores
# colocando nuevo valor entre "[]".

lista [7:9] = [100]

print lista