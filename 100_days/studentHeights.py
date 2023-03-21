#!/usr/bin/python3

# 🚨 Don't change the code below 👇
total = 0
count = 0
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
    total += student_heights[n]
    count += 1
    avg = total / count
print(student_heights)
print(total)
print(round(avg, 2))
