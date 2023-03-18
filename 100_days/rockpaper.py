#!/usr/bin/python3


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gamePlay = ['rock', 'paper', 'scissors']

myPlay = int(input("press 0 for rock, 1 for paper and 2 for scissors\n"))
myTurn = gamePlay[myPlay]

Turn2 = len(gamePlay)
random_choice = random.randint(0, Turn2 - 1)
compTurn = gamePlay[random_choice]

if myTurn == 'rock' and compTurn == 'rock':
    print(rock)
    print(rock)
    print("Draw")
elif myTurn == 'rock' and compTurn == 'paper':
    print(rock)
    print(paper)
    print("You lose: Paper beats rock")
elif myTurn == 'rock' and compTurn == 'scissors':
    print(rock)
    print(scissors)
    print("You Win: Rock beats scissors")
elif myTurn == 'paper' and compTurn == 'rock':
    print(paper)
    print(rock)
    print("You Win: Paper beats rock")
elif myTurn == 'paper' and compTurn == 'paper':
    print(paper)
    print(paper)
    print("Draw")
elif myTurn == 'paper' and compTurn == 'scissors':
    print(paper)
    print(scissors)
    print("You lose: Scissors beats paper")
elif myTurn == 'scissors' and compTurn == 'rock':
    print(scissors)
    print(rock)
    print("You lose: Rock beats scissors")
elif myTurn == 'scissors' and compTurn == 'paper':
    print(scissors)
    print(paper)
    print("You Win: Scissors beats paper")
elif myTurn == 'scissors' and compTurn == 'scissors':
    print(scissors)
    print(scissors)
    print("Draw")
