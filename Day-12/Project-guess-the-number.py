import random
import os
os.system('cls')

#PRINTING THE LOGO
from guess_the_number_logo import logo
print(logo)

number=random.randint(1,100)
#print(number)

print("WELCOME TO GUESS THE NUMBER GAME")
mode=input("Choose the mode you want to play 'easy' or 'hard' : ").lower()

def number_compare(guessed_number):
    #guess_the_number=int(input("Guess the number : "))
    if number==guessed_number:
        print(f"Your guess is correct. The hidden number is {number}")
    elif number<guessed_number:
        print("Too High")
    else:
        print("Too Low")

def guess_the_game():
    easy_level_lives=10
    hard_level_lives=5
    is_end = True
    while is_end:
        guess_the_number = int(input("Guess the number : "))
        if mode =='easy':
            number_compare(guess_the_number)
            print(f"You have still {easy_level_lives-1} left ")
            easy_level_lives -= 1
            if easy_level_lives == 0:
                print("GAME END!!")
                print(f"The hidden number is {number}")
                is_end = False
        elif mode == 'hard':
            number_compare(guess_the_number)
            print(f"You have still {hard_level_lives-1} left ")
            hard_level_lives -= 1
            if hard_level_lives == 0:
                print("GAME END!!")
                print(f"The hidden number is {number}")
                is_end = False
            

            
        
    
guess_the_game()