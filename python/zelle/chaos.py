#!/usr/bin/python3
# A simple program illustrating chaotic behaviour

def chaos():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: ") )
	for i in range(10) :
		x = 3.9 * x * (1 - x)
		print(x)

chaos()
