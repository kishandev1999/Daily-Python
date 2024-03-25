#EXERCISE
'''
LOVE CALCULATOR:
FIRST ENTER YOUR NAME AND YOUR PAIR NAME
IN YOUR BOTH NAMES CALCULATE THESE LETTERS, HOW MANY TIMES IT GOT REPEATED IN BOTH THE WORDS
'T', 'R', 'U', 'E' AND 'L', 'O', 'V', 'E'
COMBINE THESE NUMBERS TO FORM A 2DIGIT PAIR
IF IT IS GREATER THAN 90, THEN PRINT "you go together like coke and mentos"
IF IT IS IN BETWEEN 45 AND 50, THEN PRINT "you are alright together"
OTHERWISE, JUST PRINT THE SCORE
'''

#solution
name1 = input("Enter your name")
name2 = input("Enter your pair name")
combined_names = name1+name2
lower_names= combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t+r+u+e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l+o+v+e

score = int(str(first_digit) + str(second_digit))

if(score < 10) or (score >90) :
    print(f"your score is {score}, you go together like a coke and menttos")
elif (score >= 40) and (score <= 50) :
    print(f"your score is {score}, you go alright together")
else:
    print(f"your score is {score}") 
