#from replit import clear
import os
#WE ARE IMPORTING THIS MODULE TO CLEAR THE SCREEN FOR EVERY INPUT
from hangman_art import title, lives
print(title)
#STEP:1
#FINDING THE ALPHABETS IN THE GIVEN WORD:

#secret_words=["camel","marvel","instagram"]

#CHOOSE A RANDOM WORD FROM THE LIST
import random
from hangman_words import secret_words
#NOTE: ALWAYS GIVE FILENAME FROM WHERE YOU ARE IMPORTING WITH UNDERSCORE ONLY, NOT HYPHEN

chosen_word = random.choice(secret_words)
'''
or
import hangman_words
chosen_word = random.choice(hangman-words.secret_words)
'''
word_length=len(chosen_word)


display_word_blanks=[]
display_word=[]

#STEP:2
#SHOW THE BLANKS AS PER THE WORD LENGTH

for letters in range(word_length):
    display_word.append("_")

print(*display_word)
#STEP:3
#LOOP THE INPUT VARIABLE UNTIL THE CORRECT WORD IDENTIFIED
count=0
end_of_game = False
while not end_of_game:
    guess_the_word = input("Guess the letter : ").lower()
    clear = lambda: os.system('cls')
    clear()
    #clear()
    
    #IF THE GUESS WORD IS ALREADY IN THE LIST
    if guess_the_word in display_word:
        print("YOUR ALREADY GUESSED THIS WORD!!")
    
    #REPLACE THE IDENTIFIED BLANKS WITH THE CORRECT GUESS
    for letter in range(word_length):
        if guess_the_word == chosen_word[letter]:
            display_word[letter] = chosen_word[letter]
            if "_" not in display_word:
                print("YOU WON!!")
                print(f"THE GUESSING WORD IS {' '.join(chosen_word)}")
            
            
    #IF THE WORD IS WRONG, THEN WE GAVE TO REDUCE ONE LIFE
    if guess_the_word not in chosen_word:
        print(lives[count])
        count+=1
        print("WRONG GUESS!!!!")
        if count == 7:
            print("GAME OVER")
            end_of_game = True
            print(f"THE GUESSING WORD IS {' '.join(chosen_word)}")
            
            
     #ONCE, ALL LETTERS ARE IDENTIFIED, THIS CONDITIONS WILL BE MARKED AS TRUE
     #THIS WHILE LOOP ENDS       
    if "_" not in display_word:
        end_of_game=True
    print(f"{' '.join(display_word)}")
    
    
