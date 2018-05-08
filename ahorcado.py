# -*- coding: utf-8 -*-

import random
import os
from ctypes import byref, c_int

'''
Así es como se fedinen los ASCII ART
'''
IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
    'lista',
    'tuplas',
    'diccionario',
    'constantes',
    'raise',
    'accert',
    'random',
    'pass'
]


def random_word():
    index = random.randint(0, len(WORDS) - 1)
    return WORDS[index]


def display_board(hidden_word, tries):
    print('Juego del ahorcado')
    print(IMAGES[tries.value])
    print()
    print(hidden_word)
    print('--- *' * len(hidden_word))


def game(current_letter, word, tries, hidden_word):
    if current_letter not in word:
        if tries.value > 5:
            print('\nPerdiste')
            return True
        tries.value += 1
    else:
        for idx, val in enumerate(word):
            if val == current_letter:
                hidden_word[idx] = current_letter
        if '-' not in hidden_word:
            print('\nLa palabra es: {}'.format(word))
            print('\n¡Ganaste!')
            return True


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = c_int(0)
    while True:
        os.system('cls')
        display_board(hidden_word, tries)
        current_letter = str(input('Elige una letra:\t'))
        if len(current_letter) > 1 or len(current_letter) == 0:
            continue

        # Intento de solución

        if game(current_letter, word, tries, hidden_word):
            return

    # Termina solución


if __name__ == '__main__':
    run()
