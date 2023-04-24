#!/usr/bin/python3

import random
from game_data import data
from art import *
import os

def get_celebrity():
    """Function to get a randomly generated celebrity account details"""
    random_celebrity = random.choice(data)
    name = random_celebrity['name']
    description = random_celebrity['description']
    country = random_celebrity['country']
    follower_count = random_celebrity['follower_count']
    return {'name': name, 'description': description, 'country': country, 'follower_count': follower_count}

def print_celebrities(A, B):
    """Function to display the accounts to be generated, takes in two parameters and formatsthem"""
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")

def get_user_choice():
    """Getting user choice and doing error checking"""
    choice = input("Who has more followers? Type 'A' or 'B' ").upper()
    while choice not in ('A', 'B'):
        print("Invalid choice. Please try again.")
        choice = input("Who has more followers? Type 'A' or 'B' ").upper()
    return choice

def play_game():
    os.system('clear')
    print(logo)
    score = 0
    A = get_celebrity()
    B = get_celebrity()
    while A == B:
        B = get_celebrity()
    print_celebrities(A, B)
    choice = get_user_choice()
    while True:
        if choice == 'A' and A['follower_count'] > B['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
        elif choice == 'B' and B['follower_count'] > A['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        A = B
        B = get_celebrity()
        while A == B:
            B = get_celebrity()
        print_celebrities(A, B)
        choice = get_user_choice()

play_game()
