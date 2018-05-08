# -*- coding: utf-8 -*-

import turtle

def main():
	window = turtle.Screen()
	drawing = turtle.Turtle()

	draw(drawing)

def draw(drawing):
	length = int(input())
	drawing.forward(100)
	
if __name__ == '__main__':
	main()
