'''
SCENARIO:
WELCOME TO THE TIP CALCULATOR
WHAT WAS THE BILL? 124.56$
WHAT PERCENTAGE TIP WOULD YOU LIKE TO GIVE? 10, 12, or 15? 12
HOW MANY PEOPLE TO SPLIT THE BILL? 7
EACH PERSON SHOULD PAY : $19.93
'''

#example:
#If the bill was $150.00, split between 5 people with 12%tip
#Each person should pat (150.00/5) * 1.12 = 33.6666666666
#Round the result to 2 decimal places = 33.60
 
 
#SOLUTION : 
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
tip_as_percentage = tip/100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
#final_amount = round(bill_per_person, 2)
# if we use the round here, the output will be: $33.6. But, we want $33.60
#Hence, we using this below format
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay : ${final_amount}")