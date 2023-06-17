import requests

# set endpoint
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/9a586a9d448d4610d5f145facb78c9f0/flightDeals/users"


class UserManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user_data = {}
        self.first_name = ""
        self.last_name = ""
        self.email = ""

    #  used this to manually populate the sheety file, and validate the syntax of the parameters passed
    def get_destination_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        print(data)
        self.destination_data = data["users"]
        return self.destination_data

        # obtain user data, pass it back to main in an array

    def enter_user_data(self):
        # asking for information for the flight club
        print("Welcome to Rafael's Flight Club")
        print("We find the best flight deals and email them to you")
        self.first_name = input(f"What is your first name?\n")
        self.last_name = input(f"What is your last name?\n")

        email_check = True
        while email_check:
            self.email = input(f"What is your email address?\n")
            confirm_email = input(f"Enter ypur email address again?\n")
            if self.email == confirm_email:
                print("You're in the club!")
                email_check = False
            else:
                print("Email mismatch, try again")
        return self.first_name, self.last_name, self.email

    # use the above returned code to update sheety file
    def post_info(self, user_info):
        print("Here")
        print(user_info[0], user_info[1], user_info[2])
        sheet_parameters = {
            "user": {
                "firstName": user_info[0],
                "lastName": user_info[1],
                "email": user_info[2]
            }
        }
        # post the infromation for the use in the sheety users tab
        code_response = requests.post(url=f"{SHEETY_USERS_ENDPOINT}", json=sheet_parameters)
        print(code_response.json())


user_manager = UserManager()
user_data = user_manager.enter_user_data()
user_manager.post_info(user_data)
