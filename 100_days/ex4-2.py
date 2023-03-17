import random
# split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

length = len(names)
random_choice = random.randint(0, length - 1)
person = names[random_choice]
print(person + " will be paying the bill today")
