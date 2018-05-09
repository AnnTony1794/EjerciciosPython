# -*- coding: utf-8 -*-

def run():
	print('Calculadora de divisas')
	print('Convierte pesos méxicanos a pesos colombianos.')
	print('')

	a = float(input('Ingresa la cantidad:\t'))
	result = asdad(a)
	print('${} pesos méxicanos son ${} pesos colombianos'.format(a, round(result,3)))

def asdad(ammount):
	mex_to_col_rate = 145.97
	return mex_to_col_rate * ammount

if __name__ == '__main__':
	run()