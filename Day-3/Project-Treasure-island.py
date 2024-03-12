#EXERCISE:
'''
THE FLOW OF THE FINDING TREASURE IS GOES IN THIS WAY
1. IT WILL ASK YOU ARE ON CROSS ROADS, YOU WANT TO TAKE, LEFT OR RIGHT?
- IF LEFT, GO TO NEXT STEP. IF RIGHT GAME OVER
2. IF YOU CHOOSE LEFT, AGAIN IT WILL ASK YOU FOR A QUESTION:
- SWIM OR WAIT?
IF YOU CHOOSE SWIM - GAME OVER, IF YOU CHOOSE TO WAIT, AGAIN IT WILL ASK YOU ANOTHER QUESTION
3. WHICH DOOR? RED, BLUE OR YELLOW
IF YOU CHOOSE RED OR BLUE, THEN GAME OVER
IF YOU CHOOSE YELLOW - YOU WIN : YOU FIND THE TREASURE
'''
#https://ascii.co.uk/art
#This site will provide you this kind of ascii chart
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[KISHAN]
*******************************************************************************
''')
print("welcome to the TREASURE ISLAND")
print("Your Mission is to find the treasure")
name=input("What is your name? \n")
print("Lets begin our journey")
print("Choose the options accordingly. Choosing right option will help you to find the treasure")
step_1 = input("You are on the cross roads. Choose the DIRECTION: LEFT OR RIGHT? \n")

if step_1.lower() == "left":
    step_2 = input("You reached nile river bank, you want to SWIM or WAIT? \n")
    if step_2.lower() == "wait":
        print("In next 20mins, a boat will pick you up. \n")
        print("Now you crossed the river and entered into a cave")
        print("In cave, you found the boxes 1.RED BOX, 2. BLUE BOX, 3. YELLOW BOX")
        step_3=input("Choose the box, by typing is color. RED or BLUE or YELLOW \n")
        if step_3.lower() == "yellow":
            print (f"***CONGRATULATIONS {name} ***")
            print("You WIN!! YOU FOUND THE TREASURE")
        else:
            print("GAME OVER!")
            print(f"opps {name} You opened {step_3}, contains cursed stones")
    else:
        print("GAME OVER!")
        print(f"opps {name}! you caught to crocodiles")
else:
    print("GAME OVER!")
    print(f"opps {name}! you took wrong direction takes you to burning VOLCANOS")
    

