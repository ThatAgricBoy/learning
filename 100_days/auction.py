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

highest_bidder = None
highest_bid = 0

for bid in bid_diction:
    if bid["bid"] > highest_bid:
        highest_bid = bid["bid"]
        highest_bidder = bid["name"]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")
