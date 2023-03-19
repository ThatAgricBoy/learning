#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = number % 10
if last_dig > 5:
    print("Good morning")
elif last_dig < 6 and last_dig and not 0:
    print("Good afternoon")
else:
    print("Good night")
