#ROCK-PAPER-SCISSORS-GAME WITH COMPUTER
'''
ROCK PAPER SCISSORS 
ASK USER TO ENTER THE NUMBER : 0 FOR ROCK, 1 FOR PAPER, 2 FOR SCISSORS
NOW, WE WILL PLAY WITH THE COMPUTERS USING RANDOM FUNCTION
RULES:
- ROCK WINS AGAINST SCISSORS
- SCISSORS WINS AGAINST PAPER
- PAPER WINS AGAINST ROCK
'''

#SOLUTION:
import random


# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user_choice = int(input("What is your choice? 0 for ROCK, 1 for PAPER, 2 for SCISSORS \n"))
computer_choice = random.randint(0,2)

if (user_choice == 0 and computer_choice == 2):
    print("YOUR CHOICE IS : ")
    print(rock)
    print("COMPUTER CHOICE IS :" )
    print(scissors)
    print("YOU WIN!!")
elif (user_choice == 1 and computer_choice == 0):
    print("YOUR CHOICE IS : ")
    print(paper)
    print("COMPUTER CHOICE IS :" )
    print(rock)
    print("YOU WIN!!")
elif (user_choice == 2 and computer_choice == 1):
    print("YOUR CHOICE IS : ")
    print(scissors)
    print("COMPUTER CHOICE IS :" )
    print(paper)
    print("YOU WIN!!")
elif user_choice == 0 and computer_choice ==1:
    print("YOUR CHOICE IS : ")
    print(rock)
    print("COMPUTER CHOICE IS :" )
    print(paper)
    print("YOU LOST")
elif user_choice == 1 and computer_choice ==2:
    print("YOUR CHOICE IS : ")
    print(paper)
    print("COMPUTER CHOICE IS :" )
    print(scissors)
    print("YOU LOST")
elif user_choice == 2 and computer_choice ==0:
    print("YOUR CHOICE IS : ")
    print(scissors)
    print("COMPUTER CHOICE IS :")
    print(rock)
    print("YOU LOST")
else:
    print("draw")