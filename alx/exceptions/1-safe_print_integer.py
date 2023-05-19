#!/usr/bin/python3

"""
This function prints integer
print integer followed by newline
handle any type of data
return true if value is integer
print using .format()
"""
def safe_print_integer(value):
	try:
		print("{:d}".format(value))
	except:
