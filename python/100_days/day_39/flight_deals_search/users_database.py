import requests

print("""Welcome to the Flight Club
We find the best flight deals and email you 
""")
FIRSTNAME = input("What is your first name: \n")
LASTNAME = input("What is your last name: \n")
email_check = True
while email_check:
    EMAIL = input("What is your email: \n")
    EMAIL_VALIDATION = input("Type your email again: \n")
    if EMAIL == EMAIL_VALIDATION:
        email_check = False
    else:
        print("double check your email")
user_api = "https://api.sheety.co/9a586a9d448d4610d5f145facb78c9f0/flightDeals/users"

data = {
    "user": {
        "firstName": FIRSTNAME,
        "lastName": LASTNAME,
        "email": EMAIL,
    }
}
response = requests.post(url=user_api, json=data)
print(response.text)
print("Your Email has been added successfully")