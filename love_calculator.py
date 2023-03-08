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

false =  mystr.lower().count('f') + mystr.lower().count('a') + mystr.lower().count('l') + mystr.lower().count('s') + mystr.lower().count('e')

score = str(true) + str(false)
print(score)

