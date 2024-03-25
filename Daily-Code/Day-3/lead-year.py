#check whether the year is leap year or not
#LOCIC :
'''
IF THE YEAR IS DIVISIBLE BY 4 
DIVISIBLE BY 100 AND
DIVISIBLE BY 400
THEN ONLY WE CONSIDER IT AS LEAP YEAR
'''

#SOLUTION
year = int(input("Enter the year : "))

if year %4 == 0 :
    if year%100 == 0 :
        if year%400== 0 :
            print("It is a LEAP YEAR")
        else:
            print("Not a LEAP YEAR")
    else:
        print("Not a LEAP YEAR")
else:
    print("Not a LEAP YEAR")