#!/usr/bin/python3

# Adds even numbers between 1 and 100
total = 0
for i in range (1, 101):
    if i % 2 == 0:
        total += i
print(total)
