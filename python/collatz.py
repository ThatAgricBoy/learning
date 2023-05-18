def collatz(number):
	if number % 2 == 0:
		return number // 2
	elif number % 2 == 1:
		return 3 * number + 1
while True:
	try:
		num = int(input('Enter a nunber: \n'))
		break
	except ValueError:
		print("Error: Enter a valid number")
	i = num
while i != 1:
	print(i)
	i = collatz(i)
print(1)
