# Program finds how many days, weeks,

# months we have left if we live until 90 years old.

age = input("What is your current age\n")

old_age = 90
new_age = 90 - int(age)

days_left = new_age * 365

weeks_left = round((new_age * 52))

months_left = round(new_age * 12)

message = (f"You have {days_left} days, {weeks_left} weeks, and {months_left} left")

print(message)
