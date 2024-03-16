import random
import os
from art import logo,vs
from data import data
os.system('cls')

#CHOOSING THE RANDOM PERSON NAME

#print(data[0]['name'])
raw_option=""



'''
def compare_persons(guess):
    score = 0
    
        #option_B=random.choice(data)
        
    elif (guess == 'b') and (option_A['follower_count'] < option_B['follower_count']):
        #option_A=random.choice(data)
    else:
        return 0
'''
option_A=random.choice(data)
option_B=random.choice(data)

        
def high_low_game():
    is_continue = True
    global option_A, option_B
    option_C=""
    score =0
    while is_continue:
        print(logo)
        print(f"YOUR SCORE IS : {score}")
        print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
        #data.remove(option_A)
        print(vs)
        
        print(f"Against B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}")
        #data.remove(option_B)
        user_guess=input("Guess who has more followers : ").lower()
        

        if (user_guess == 'a') and (option_A['follower_count'] > option_B['follower_count']):
            #print(option_A['follower_count'])
            score+=1
            option_B=random.choice(data)
            os.system('cls')
        elif (user_guess == 'b') and (option_A['follower_count'] < option_B['follower_count']):
            score+=1
            option_A=option_B
            option_B=random.choice(data)
            os.system('cls')
        elif (user_guess != 'a') and (user_guess != 'b'):
            os.system('cls')
            #print("#############################")  
            print("*******WRONG INPUT**********")
            print("TRY AGAIN - CHOOSE EITHER 'A' OR 'B'")
            #print("#############################")  
        else:
            print("GAME OVER")
            is_continue = False
    
    print("\n")
    print("#############################")        
    print(f"YOUR FINAL SCORE IS {score}")
    print("#############################")  
            
        


high_low_game()        

'''
 if output == 0:
            print("GAME OVER")
            is_continue = False
        else:
            score+=1
            print(score)
'''
    
    
    
    
        