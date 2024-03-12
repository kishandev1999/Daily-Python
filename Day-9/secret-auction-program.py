import os
from secret_auction_logo import logo
os.system('cls')

#PRINTING THE LOGO
print(logo)

#CREATING THE EMPTY DICTIONARY:
bidding_details={}

bidding_end = True

#AUCTION RESULTS CHECKER
def bidding_record(bids):
    highest_bid = 0 
    winner=""   
    for key in bidding_details:
        if bidding_details[key] > highest_bid:
            highest_bid = bidding_details[key]
            winner=key
            print(f"The highest bidding winner is {winner} with amount ${highest_bid}")

#ITERATING THE USER NAME AND AMOUNT AS INPUTS
while bidding_end :
    name=input("Enter your name : ")
    amount=int(input("Enter the amount you want to bid : $"))
    bidding_details[name]=amount
    repeat=input("If you want to continue, type 'yes' or else type 'no' : ").lower()
    #print(bidding_details)
    if repeat == "no":
        bidding_end = False
        print("AUCTION ENDED")
        bidding_record(bidding_details)
    elif repeat == "yes":
        os.system('cls')
    
            
            
            
#REFERENCE:
#https://pythontutor.com/python-compiler.html#mode=edit
#IF YOU WANT TO VISUALIZE THE CODE OR LISTED OF DICTIONARIES, YOU CAN GO THROUGH THIS LINK


    
    
