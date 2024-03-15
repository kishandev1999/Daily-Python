import os
import random
os.system('cls')

from blackjack_logo import logo
print(logo)
#DECK:  
cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards=random.sample(cards_list,2)
computer_cards=random.sample(cards_list,2)
is_game_over = False
user_new_card=random.choice(cards_list)
computer_new_card=random.choice(cards_list)


'''
THIS FUNCTION WILL CALCULATE THE SCORE OF CARDS
AND RETURN THE SUM OF THE CARDS FOR THE USER AND THE COMPUTER
'''
def calculate_score(cards):
    if sum(cards) == 21:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards_list.remove(11)           
        cards_list.append(1)

    
    return sum(cards)
    
def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"


    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
    
while not is_game_over:
    user_score =calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards : {user_cards}, current score is {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or int(user_score) > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass : ")
        if user_should_deal.lower()=='y':
            user_cards.append(user_new_card)
        else:
            is_game_over = True
            
            
while computer_score !=0 and computer_score <17:
    computer_cards.append(computer_new_card)
    computer_new_card = calculate_score(computer_cards)
    
print(f"Your final hand : {user_cards}, final score: {user_score}")
print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")

print(compare(user_score,computer_score))
    