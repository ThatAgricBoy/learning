#!/usr/bin/python3

# Love calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
mystr = name1 + name2
true = mystr.lower().count('t') + mystr.lower().count('r') + mystr.lower().count('u') + mystr.lower().count('e')

false =  mystr.lower().count('l') + mystr.lower().count('o') + mystr.lower().count('v') + mystr.lower().count('e')

score = true + false

if score < 10 or score  > 90:
	print(f"Your score is {score}, you go together like coke and mentos.")
