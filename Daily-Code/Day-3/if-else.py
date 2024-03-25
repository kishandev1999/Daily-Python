#IF-ELSE CONDITION
#FORMAT
'''
if condition
    print(statement)
else
    print(statement)
'''

#Exercise-1
'''
Now, you can check height of each person
If the height is more that 120cm then that person is allow for a ride
'''
#Solution
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?"))

if (height >= 120) :
    print("You can ride the rollercoaster")
else:
    print("Sorry, you are not allowed to ride. Grow taller")
    
#COMPARISION OPERATORS
'''
 > - GREATER THAN
 < - LESS THAN
 >= - GREATER THAN OR EQUAL TO
 <= - LESS THAN OR EQUAL TO
 == - EQUAL TO
 != -- NOT EQUAL TO
'''
#NOTE: ONE EQUAL SIGN (=) MEANS ASSIGNING VALUE TO THE VARIABLE
#TWO EQUAL SIGNS MEANS, IT IS COMPARATOR


#EXERCISE-2
'''
PRINT THE NUMBER IS EVEN OR ODD
'''
#solution
number = int(input())
if(number%2 == 0):
    print("This is EVEN number")
else:
    print("This is ODD number")


#NESTED IF STATEMENTS
'''
if condition1:
    do A
elif condition2:
    do B
else:
    do C
'''


#EXERCISE-3
'''
CHECK THE HEIGHT FIRST, IF THE HEIGHT IS GREATER THAN 120 CMS, THEN CHECK THE AGE
BASED ON THE AGE, CHARGE THE ROLLER-COSTER TICKET
IF AGE IS GREATER THAN 12, CHANGE 5$
IF AGE IS GREATER THAN OR EQUAL TO 18, CHARGE 7$
IF AGE IS NOT GREATER THAN 18, THEN CHARGE 12$
IF THE HEIGHT IS NOT GREATER THAN OR EQUAL TO 120CM, DON'T ALLOW
'''

height=int(input())
age=int(input())

if height >=120 :
    print("You are allowed for a roller coster ride")
    if age < 12 :
        print("Please pay $5")
    elif age <=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("sorry, you are not allowed for a roller coster ride")