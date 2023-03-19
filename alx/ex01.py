#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{}".format(number))
    print("You are welcome")
    print("Thank you")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
