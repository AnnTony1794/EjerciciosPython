# -*- coding: utf-8 -*-

import random

def run():
    intentos = 1
    rango = int(input('Ingresa el número mayor que se generará:\t'))
    num = int(input('Ingresa un número:\t'))
    ran = random.randint(1, rango)

    while num != ran:
        if num < ran:
            print('El número es más grande.')
        elif num > ran:
            print('El número es más pequeño.')
        num = int(input('Ingresa un número:\t'))
    print('Encontraste el número!!!')


if __name__ == '__main__':
    run()