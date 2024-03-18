#COFFEE MACHINE CAN DISPENSE THREE TYPES OF COFFEES :
'''
|  COFFEE         |   |          CONTENTS                    | |  COST  |
1. ESPRESSO         -   5Oml WATER + 18g COFFEE                 - $1.50 
2. LATTE            -   200ml WATER + 24g COFFEE + 150ml MILK   - $2.50
3. CAPPUCCINO       -   250ml WATER + 24g COFFEE + 100ml MILK   - $3.00 
'''
#COIN DENOMINATION
'''
PENNY   -  1cent      -  $0.01
NICKLE  -  5cent      -  $0.05
DIME    -  10cent     -  $0.10
QUARTER -  25cent     -  $0.25
'''
#TOTAL CONTENTS IN THE MACHINE
'''
WATER  - 300ml
MILK   - 200ml
COFFEE - 100g  
'''
import os
os.system('cls')
quantity_in_the_machine = {'water':1300,'milk':1200,'coffee':100}



def coffee_machine_data():
    for keys in quantity_in_the_machine:
            print(f"{keys}:{quantity_in_the_machine[keys]}")
    #print(f"Money:${money}")
    
def coffee_empty():
    if quantity_in_the_machine['water'] <0:
        print("Sorry, there is not enough water")
    elif quantity_in_the_machine['milk'] <0:
        print("Sorry, there is not enough milk") 
    elif quantity_in_the_machine['coffee'] <0:
        print("Sorry, there is not enough coffee")

def coffee_calculator(machine_input):
        
    if machine_input == 'report':
        coffee_machine_data()
    elif machine_input == 'espresso':
        quantity_in_the_machine['water'] -= 200
        quantity_in_the_machine['coffee'] -= 18
        #coffee_machine_data()
        coffee_empty()
        #print(f"{quantity_in_the_machine}")
    elif machine_input == 'latte':
        quantity_in_the_machine['water'] -= 200
        quantity_in_the_machine['milk'] -= 150
        quantity_in_the_machine['coffee'] -= 24
        #coffee_machine_data()
        coffee_empty()
    elif machine_input == 'cappuccino':
        quantity_in_the_machine['water'] -= 250
        quantity_in_the_machine['milk'] -= 100
        quantity_in_the_machine['coffee'] -= 24
        #coffee_machine_data()
        coffee_empty()
    elif machine_input == 'end':
        print("*******POWER OFF**********")
    else:
        print("PROVIDE CORRECT INPUT")
        
        
def coin_insert():
    quarter_input=float(input("How many quarters? "))
    dime_input=float(input("How many dimes? "))
    nickle_input=float(input("How many nickles? "))
    penny_input=float(input("How many pennies? "))
    quarter_count=quarter_input*0.25
    dime_count=dime_input*0.10
    nickle_count=nickle_input*0.05
    penny_count=penny_input*0.01
    count=quarter_count+dime_count+nickle_count+penny_count
    return count
    

def coffee_machine():
    is_continue=True
    while is_continue:
        total_money=0
        espresso_cost=1.50
        latte_cost=2.50
        cappuccino_cost=3.00
        user_input=input("What would you like? (espresso/latte/cappuccino): ").lower()        
        coin_insert_output=coin_insert()
        if user_input == 'espresso' and coin_insert_output >=espresso_cost:
            coffee_calculator(user_input)
            total_money+=espresso_cost
            change=round(coin_insert_output-espresso_cost,2)
            print(f"Money : {round(total_money,2)}")
            print(f"Here is your ${change} change")
        elif user_input == 'latte' and coin_insert_output>=latte_cost:
            coffee_calculator(user_input)
            total_money+=latte_cost
            change=round(coin_insert_output-latte_cost,2)
            print(f"Money : {round(total_money,2)}")
            print(f"Here is your ${change} change")
        elif user_input == 'cappuccino' and coin_insert_output>=latte_cost:
            coffee_calculator(user_input)
            total_money+=cappuccino_cost
            #print(f"Money : {total_money}")
            change=round(coin_insert_output-cappuccino_cost,2)
            print(f"Here is your ${change} change")
        else:
            print("****INPUT AMOUNT IS IN CORRECT****")
coffee_machine()

