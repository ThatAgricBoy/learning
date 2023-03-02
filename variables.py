# This programs says hello world and ask for your name

print('Before we go an further')

print("What is your name")
myName = input('My name is: ')

print('It is good to meet you, ' + myName)

print('The length of your name is: ')

print(len(myName))

print('What is your age? ')

myAge = input()

print('You will be ' + str(int(myAge) + 1) + ' in a year')

# This line of code gets input from user
# then finds the length of the input
# because we can only add strings to strings we have
# to use the str function to add the result
# then it uses the len function to calculate the
# the length of input from the user
print("The length of your name is " + str(len(input("Enter your second name: "))))
