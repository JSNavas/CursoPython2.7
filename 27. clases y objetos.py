import os

class Diario:

	def __init__(self):
		self.lista = []

	def escribirEnDiario(self):
		Diario.limpiarP()
		print "\t\t\t   |  ESCRIBIR EN DIARIO  |"
		escribir = raw_input(" Escriba aqui: \n\n > ")
		self.lista.append(escribir + "\n")

		raw_input("\n 'Guardado en el diario'")

	def mostrarDiario(self):
		Diario.limpiarP()
		print "\t\t\t     |  MOSTRAR DIARIO  |"

		for elemento in self.lista:
			print " > " + elemento

	def limpiarP(self):
		os.system("clear")

Diario = Diario()

Diario.escribirEnDiario()
Diario.mostrarDiario()
