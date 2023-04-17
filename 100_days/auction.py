#!/usr/bin/python3

import os
from art import logo

print("Welcome to Max online auction program")
print(logo)

bid_diction = []

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidder = {"name": name, "bid": bid}
    bid_diction.append(bidder)

    bid_again = input("Do you want to bid again? Type 'yes' or 'no': ").lower()

    if bid_again == "no":
        break

    os.system('clear')

print("\nThe auction has ended.\n")

highest_bid = max(bid_diction, key=lambda x:x["bid"])
print(f"The winner is {highest_bid['name']} with a bid of ${highest_bid['bid']}!")    

