# Diccionarios

# En los diccionarios los elementos no tienen un indice si no una clave
# y se declaran: el nombre del diccionario, entre llaves la clave
#"{'clave':1,2,3,4[1,2,3,4]}" y luego ":" despues de la clave para
# introducir los valores que va a tener esa clave.

d = {'clave': 1,2,3[1,2,3,4,5]}

print "El contenido del diccionario 'clave' es: "
print d['clave']

# Tambien se puede diferentes claves, separandolas por "," y se pueden
# modificar los valores que contenga cada diccionario, menos la clave.

d = {'clave': [1,2,3,4,5],'clave2': "contenido de la clave2"}

# Es importante saber que como clave se puede usar cualquier tipo
# de dato, incluso tuplas, a exepcion de listas y diccionarios.

print "------------------------------------------"
print "El contenido del diccionario 'clave' es: "
print d['clave']
print
print "El contenido del diccionario 'clave2' es: "
print d['clave2']

# Para cambiar un valor de un diccionario se coloca el nombre del
# diccionario, entre corchetes ['la clave'] el signo de " = " y
# se coloca el valor que se le desea asignar

print "------------------------------------------"
print "El nuevo contenido de 'clave' es: "
d['clave'] = 0,0,0,0,0

print d['clave']

