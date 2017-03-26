class Fecha(object):

    def __init__(self):
        self.__dia = 1


	def getDia(self):
		return self.__dia


	def setDia(self, dia):
		self.__dia = 28

	dia = property(getDia, setDia)


Fecha = Fecha()

Fecha.dia = 33
print Fecha.dia