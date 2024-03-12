'''
FROM THE BELOW STRING_INPUT : YOU'LL FIND THE PEOPLE NAMES
NOW, YOU HAVE TO RANDOMLY SELECT A PERSON WHO PAYS THE BILL
'''
import random

names_input = "kishan Dev, Satish, Arun Kanth, Datta"
names = names_input.split(', ')
num_items = len(names)-1
random_name = random.randint(0,num_items)
person_will_pay = names[random_name]

print(f"{person_will_pay} will pay the bull today")

