#EXERCISE-3
'''
CHECK THE HEIGHT FIRST, IF THE HEIGHT IS GREATER THAN 120 CMS, THEN CHECK THE AGE
BASED ON THE AGE, CHARGE THE ROLLER-COSTER TICKET
IF AGE IS GREATER THAN 12, CHANGE 5$
IF AGE IS GREATER THAN OR EQUAL TO 18, CHARGE 7$
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
    else:
        bill = 12
        print("Please pay $12")
        
    wants_photo = input("Do you want a photo taken? Y OR N" )
    if wants_photo == "Y" :
        bill +=3
else:
    print("sorry, you are not allowed for a roller coster ride")