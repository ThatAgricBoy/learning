#!/usr/bin/python3
student_scores = input("Input a list of student scores ").split()
highest = 0
for n in range(0, len(student_scores)):
	student_scores[n] = int(student_scores[n])
	if student_scores[n] > highest:
		highest = student_scores[n]
print(student_scores)
print("The highest score is {}".format(highest))
