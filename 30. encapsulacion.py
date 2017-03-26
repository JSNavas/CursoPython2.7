# Se declara un atributo o metodo privado, al escribir
# antes del nombre 2 guiones bajos

class Lista:
	def __init__(self):
		self.xLista = [1,2,3,4,5] 	  # Lista publica
		self.__xLista = [6,7,8,9,10]  # Lista privada

	def metodo(self):				  # Metodo publico
		print "Metodo publico"

	def __metodo(self):				  # Metodo privado
		print "Metodo privado"

									  # Para acceder al atributo privado,
									  # se crea un nuevo metodo que retorne
									  # el atributo privado
	def getPrivado(self):		 
		return self.__xLista

									  # Para modificar el atributo privado
									  # se crea otro metodo que modifique el
									  # atributo privado

	def setPrivado(self):
		self.__xLista = [34,65,78,98]

Lista = Lista()

print "Lista publica:", Lista.xLista
print "Lista privada:", Lista.getPrivado()				# Se realiza la llamada del atributo privado
														# a traves de la funcion "getPrivado()" que
														# retorna el atributo para ver su contenido

print
Lista.setPrivado()										# Se llama a la funcion que modifica el atributo
														# privado y luego la funcion que lo retorna para
														# mostrar su contenido y ver el cambio
print "Lista privada modificada:", Lista.getPrivado()	
