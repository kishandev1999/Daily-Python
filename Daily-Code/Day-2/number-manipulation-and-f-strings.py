#NUMBER MANIPULATION
print(8/3) #output : 2.666666666666666
print(int(8/3)) #output : 2
print(round(8/3)) #output : 3
#IN ROUND, IF IT IS 2.6 IT WILL ROUND TO 3. IF IT IS 2.4, IT WILL ROUND TO 2
print(round(8/3,2)) #output : 2.67
#This will round upto 2 digits

#FLOOR DIVISION
print(8//3) #output :2
#This will print the near integer. This data type is integer 

#SHORTCUTS
score =0
score = score + 1 #OR
score +=1
#likely +=, -=, /=, *=, /=

#If you want to print a integer, then 
print("your score is " + str(score))

#F-STRING
score=0
height = 5.7
isWinning = True
#f-string
print(f"your score is {score} and your height is {height}, you are winning {isWinning}")

 