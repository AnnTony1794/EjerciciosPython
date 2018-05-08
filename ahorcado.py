# -*- coding: utf-8 -*-

import random
import os

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
	index = random.randint(0, len(WORDS)- 1)
	return WORDS[index]

def display_board(hidden_word, tries):
	print(IMAGES[tries])
	print()
	print(hidden_word)
	print('--- *' * len(hidden_word))

def run():
	word = random_word()
	hidden_word = ['-'] * len(word)
	tries = 0
	while True:
		display_board(hidden_word, tries)
		current_letter = str(input('Elige una letra:\t'))
		os.system('cls')

		if current_letter in word:
			hidden_word 

if __name__ == '__main__':
	print('Juego del ahorcado')
	run()