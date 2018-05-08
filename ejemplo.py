# -*- coding: utf-8 -*-

class Personaje():

	vida = 100
	nombre = ""
	clase = ""

	def __init__(self, vida, nombre, clase):
		self.vida = vida
		self.nombre = nombre
		self.clase = clase

	def atacar(self, personaje, dano):
		personaje.vida -= dano
		if personaje.vida < 0:
			personaje.vida = 0
		print('La vida de {} es {} '.format(personaje.nombre , personaje.vida))

def run():

	print('Hola')

	pepe = Personaje(10, "Pepe", "Rana")
	rana = Personaje(10, "Rana", "Pepe")

	while pepe.vida > 0 and rana.vida > 0:

		quien = int(input('Quien ataca?\n1)\tPepe\n2)\tRana'))
		if quien == 1:
			pepe.atacar(rana, 6)
		elif quien == 2:
			rana.atacar(pepe, 2)

	if pepe.vida <= 0:
		print('Ganó la rana')
	else:
		print('Ganó pepe')

if __name__ == '__main__':
	run()
