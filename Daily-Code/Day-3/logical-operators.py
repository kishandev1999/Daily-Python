#LOGICAL OPERATORS:
'''
1. AND
IF BOTH CONDITIONS ARE TRUE, THEN ONLY THE OUTPUT WILL BE TRUE, ELSE IT WILL BE FALSE
EXAMPLE :
a=12
a >10 and a < 13 
OUTPUT:
True

2. OR
IF ANY CONDITION CAN SATISFY, THE OUTPUT WILL BE TRUE, ELSE IT WILL BE FALSE
EXAMPLE :
a=12
a < 17 or a < 14
OUTPUT:
True

3. NOT
IF CONDITION IS TRUE, IT PRINT AS FALSE, VICEVERSA
EXAMPLE:
a=12
not a > 15
OUTPUT:
True
'''

#EXERCISE
'''
CHECK THE HEIGHT FIRST, IF THE HEIGHT IS GREATER THAN 120 CMS, THEN CHECK THE AGE
BASED ON THE AGE, CHARGE THE ROLLER-COSTER TICKET
IF AGE IS GREATER THAN 12, CHANGE 5$
IF AGE IS GREATER THAN OR EQUAL TO 18, CHARGE 7$
IF AGE IS GREATER THAN OR EQUAL TO 45 AND LESS THAN OR EQUAL TO 55, THEN PRINT "Everything is going to be ok. Have a free ride in us!"
IF AGE IS NOT GREATER THAN 18, THEN CHARGE 12$
IF ALL CONDITIONS ARE SATISFIED, THEN ASK THEM IF THEY WANT A PHOTO.
IF THEY WANT, THEN ADD 3$ TO THEIR BILL
IF THE HEIGHT IS NOT GREATER THAN OR EQUAL TO 120CM, DON'T ALLOW
'''

height=int(input())
age=int(input())

if height >=120 :
    print("You are allowed for a roller coster ride")
    if age < 12 :
        bill = 5
        print("Please pay $5")
    elif age <=18:
        bill = 7
        print("Please pay $7")
    elif age >=45 and age <=55:
        print("Everything is going to be ok. Have a free ride in us!")
    else:
        bill = 12
        print("Please pay $12")
        
    wants_photo = input("Do you want a photo taken? Y OR N" )
    if wants_photo == "Y" :
        bill +=3
else:
    print("sorry, you are not allowed for a roller coster ride")
