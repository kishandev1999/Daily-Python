#EXERCISE
'''
SUM ALL THE EVEN NUMBERS WITH IN THE RANGE OF 1 TO 100
'''

#SOLUTION
target = int(input("Enter your range : "))
total=0
for num in range(0,target+1,2):
    #print(num, end= " ")
    total+=num
    
print(f"The sum of even number with in the target-{target} range is : {total}")

