class Ejemplo:
	def __init__(self):
		self.__lista = [1,2,3,4]

	def publico(self):
		print "Publico"


	def __privado(self):
		print "Privado"

ej = Ejemplo()
ej.publico()

#ej.__privado()

ej._Ejemplo__privado()			# Metodo privado

print ej._Ejemplo__lista   		# Lista privada