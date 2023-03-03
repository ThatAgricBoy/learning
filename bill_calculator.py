# This program calculates the bill plus the
# tip split betwwen a certain number of people

print("Welcome to the tip calculator!")
bill = input("What was the total bill? \n")
new_bill = float(bill)

percent = input("How much tip would you like to give? 10, 12, 0r 15? ")

new_percent = int(percent) / 100

tip = (new_bill * new_percent)
total_bill = new_bill + tip
persons = input("How many people to split the bill? ")

new_person = int(persons)

bill_per_person = round((total_bill / new_person), 2)

print(bill_per_person)
