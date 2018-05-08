# -*- coding: utf-8 -*-

def run():
	x = int(input('Introduce la base del cuadrado:\t\t'))
	y = int(input('Introduce la altura del cuadrado:\t'))

	#hacer_cuadrado(x, y)

	square = Square()
	square.make_square(x, y)


class Square():
	def make_square(self, x, y):
		sq = ''
		for i in range(0, y):
			for j in range(0, x):
				sq += '* '
			sq += '\n'
		print(sq)

def hacer_cuadrado(x, y):
	sq = ''

	for i in range(0, y):
		for j in range(0, x):
			sq += '* '
		sq += '\n'
	print(sq)


if __name__ == '__main__':
	run()