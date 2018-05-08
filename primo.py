# -*- coding: utf-8 -*-

def run():
	number = int(input('Escribe un número:\t'))
	result = is_prime(number)
	if result:
		print('Sí es primo.')
	else:
		print('No es primo.')

def is_prime(number):
	if number < 2:
		return False
	elif number == 2:
		return True
	elif number % 2 == 0:
		return False
	else:
		for i in range(3, number + 1):
			if number % i == 0:
				return False
			else:
				return True

if __name__ == '__main__':
	run()