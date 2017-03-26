# encoding: utf-8

dic = {'nombre': "", 'apellido': ""}

print
dic['nombre'] = raw_input("Ingrese su nombre: ")
dic['apellido'] = raw_input("Ingrese su apellido: ")

print
print dic['nombre'], dic['apellido']

print
print "(1) Si desea eliminar su nombre."
print "(2) Si desea eliminar su apellido. \n"

n = input()

if n == 1:
    print "\n[Al presionar ENTER se eliminara su nombre...] \n"
    raw_input()

# Se usa la funcion "del" eliminar una clave
# de un diccionario

    del (dic['nombre'])

    print "Se ha eliminado su nombre. \n"
    print dic['apellido']

if n == 2:
    print "\n[Al presionar ENTER se eliminara su apellido...] \n"
    raw_input()
    del (dic['apellido'])
    print "Se ha eliminado su apellido. \n"
    print dic['nombre']

# Para eliminar un diccionario (dejarlo vacio) se utiliza la funcion ".clear()"
# se utiliza nombrando el diccionario que queremos eliminar antes de la funcion
# "diccionario.clear()"
