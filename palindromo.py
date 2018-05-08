# -*- coding: utf-8 -*- 

def run():
    palindromo = input('Ingresa una palabra:\t')
    palabra_al_reves = []

    for letter in palindromo:
        palabra_al_reves.insert(0, letter)

    palindromo_true = ''.join(palabra_al_reves)

    if palindromo_true == palindromo:
        print('Sí es palindromo')
    else:
        print("No es palindromo")
if __name__ == '__main__':
    run()