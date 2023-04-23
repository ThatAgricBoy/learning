#!/usr/bin/python3

import random
import os
from art import guess_logo

print("Welcome to the Number Guessing Game")

"""creating the list to hold the numbers to be guesses"""
num_list = []
for i in range(1, 101):
    num_list.append(i)

"""function to start the game"""
def start_game():
    print(guess_logo)
    the_random_number = random.choice(num_list)
    
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        num_of_guess = 10
        print(f"You have {num_of_guess} attempts remaining to guess the number.")
    else:
        num_of_guess = 5
        print(f"You have {num_of_guess} attempts remaining to guess the number.")
    while num_of_guess > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess == the_random_number:
            print(f"You got it! The answer was {the_random_number}")
            break
        elif user_guess < the_random_number:
            num_of_guess -= 1
            print(f"You guessed too low. {num_of_guess} guesses left.")
        else:
            num_of_guess -= 1
            print(f"You guessed too high. {num_of_guess} guesses left.")
            
        if num_of_guess == 0:
            print(f"Game over. The number was {the_random_number}.")
            break

start_game()
play_again = input("do you want to play another game type Y = yes and N = no ").lower()
while play_again == "y":
    os.system('clear')
    start_game()
