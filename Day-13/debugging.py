############DEBUGGING#####################
'''
TIPS AND EXERCISES FOR DEBUGGING
'''

# 1.Describe Problem
# QUESTION: #HERE IT WON'T PRINT 20. WHY? 
def my_function():
   for i in range(1, 20):
     if i == 20:
       print("You got it")
       
my_function()

#ANSWER:
'''
BECAUSE THE RANGE FUNCTION WILL SHOW THE VALUES TILL 19. NOT SHOW 20
SO, WE HAVE TO GIVE range(1,21). TO PRINT THE STATEMENT
'''

######################################################
# 2. Reproduce the Bug
#QUESTION: WE ARE GETTING THE ERROR SOMETIMES. WHY?
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

#ANSWER
'''
HERE WE ARE GIVING THE RANGE TILL 1,6 MEANS AS PER THE LIST IT IS 0,1,2,3,4,5,6
IT WILL THROW AN ERROR, "INDEX OUT OF RANGE"
HENCE, MODIFY THIS LINE : dice_num = randint(0, 5)
'''

#######################################################

# 3. Play Computer
#QUESTION : WHEN WE PUT THE YEAR 1994. IT PRINTS NOTHING. WHY?
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")
    
#ANSWER:
'''
BECAUSE, WE HAVE TO PROVIDE THE >= IN ELIF STATEMENT
HENCE, MODIFY THIS LINE : elif year >=1994
'''

######################################################
# 4. Fix the Errors
#FIND OUT WHAT ARE THE ERRORS IN THE CODE AND FIX IT
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")

#ANSWER
'''
1.FIRST FIX THE INDENTATION
2.IN input() function, IT WILL TAKE AS STRING AND YOU ARE COMPARING THE STRING VALUE > 18
So, do type conversion. Modify the line age=int(input("How old are you?"))
'''

###################################################
# 5. Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
'''
TO DEBUG, TRY TO FIND OUT THE RESULT AT EVERY STAGE OR STEP
SO, TRY TO USE THE PRINT STATEMENT AND GET TO KNOW THE RESULTS
HENCE, MODIFY THIS LINE : word_per_page = int(input("Number of words per page: "))
'''
#########################################################

# 6. Use a Debugger
#HERE WE NEED THIS LIST[2,4,6,8,10,26] as OUTPUT. BUT, WE ARE GETTING ONLY OUTPUT[26]. WHY?
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

#ANSWER:
'''
WE HAVE TO GIVE THE INDENTATION AND RUN THIS INSIDE THE FOR LOOP
HENCE, GIVE A INDENTATION AND MOVE THIS LINE INSIDE THE FOR LOOP: b_list.append(new_item)
'''

#THE DEBUGGER SOFTWARES:
#https://pythontutor.com/
#https://thonny.org/


#TIPS TO DEBUGGING:
'''
7. TAKE A BREAK
8. ASK YOUR FRIEND (OR) DEVELOPER (OR) COLLEAGUE
9. RUN YOUR CODE OFTEN
10. USE STACKOVERFLOW
'''


#EXERCISES:
#1. EVEN OR ODD
number = int(input()) # Which number do you want to check?

if number % 2 = 0: 
  print("This is an even number.")
else:
  print("This is an odd number.")
#ANSWER
'''
COMPARATOR OPERATION IS WRONG
MODIFY THIS LINE : if number % 2 == 0: 
'''

#2. LEAP YEAR
# Which year do you want to check?
year = input()

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
#ANSWER
'''
INPUT DATATYPE IS WRONG
MODIFY THIS LINE : year = int(input())
'''

#3. FIZZ BUZZ PROGRAM:
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
    
#ANSWER
'''
LOGICAL OPERATOR IS WRONG
MODIFY THIS LINE : if number % 3 == 0 and number % 5 == 0:
BOTH CONDITIONS NEED TO SATISFY
'''