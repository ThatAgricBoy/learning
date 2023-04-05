#!/usr/bin/python3
"""
	This function will print x element in a list
	print list on same line
	return real number of numbers printed
	use try and except
"""
def safe_print_list(my_list=[], x=0):
	count = 0
	for i in range(x):
		try:
			print("{}".format(my_list[i]), end="")
		except IndexError:
			break
		else:
			count += 1 
	print()
	return count
