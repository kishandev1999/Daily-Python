from game_data import celeb_data
from art import logo
from guess_model import Guess
import random
from compare_brain import CompareBrain

guess_list=[]
for i in range(len(celeb_data)):
    celeb_name=celeb_data[i]['name']
    celeb_description=celeb_data[i]['description']
    celeb_follower=celeb_data[i]['follower_count']
    celeb_country=celeb_data[i]['country']
    guess=Guess(celeb_name,celeb_description,celeb_follower,celeb_country)
    guess_list.append(guess)



equate = CompareBrain(guess_list)
equate.pop_two_question()
#equate.compare()
    

    
