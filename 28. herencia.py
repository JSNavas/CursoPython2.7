class Personaje:

	def __init__(self):
		self.vida = 3

	def hablar(self, mensaje):
		print mensaje

	def AumentarVida(self):
		self.vida += 1
		print "+1 vida:", self.vida

	def PerderVida(self):
		self.vida -= 1
		print "-1 vida:",self.vida

class Mario(Personaje):
	lanzarFuego = 0

	def Met_lanzarFuego(self):
		self.lanzarFuego += 1
		print "Puedo lanzar fuego!!"

class Luigi(Personaje):
	lanzarHielo = 0

	def Met_LanzarHielo(self):
		self.lanzarHielo += 1
		print "Puedo lanzar hielo!!"

Mario = Mario()
Luigi = Luigi()

Mario.hablar("Soy Mario")
Mario.AumentarVida()
Mario.Met_lanzarFuego()

print

Luigi.hablar("Soy Luigi")
Luigi.PerderVida()
Luigi.Met_LanzarHielo()


		
		