# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#Don't change the code above

#Write your code below this line

bmi = round(weight / height ** 2)

# Interpreting the bmi of the user

if bmi <= 18.5:
 print("Your BMI is 18, you are underweight ")
elif bmi < 25:
 print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
 print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
 print(f"Your BMI is {bmi}, you are obese.")
else:
 print(f"Your BMI is {bmi}, you are clinically obese.")
