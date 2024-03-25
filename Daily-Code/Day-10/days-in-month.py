# Find the number of days in a month based on the year
#inputs will be like : year and month_number
'''
year : 2023
month : 5
'''

#First we need to find out whether the year is leap year or not
#because, in leap year FEBRUARY has 29 days

year=int(input("Enter the year : "))
month=int(input("Enter the month : "))

def is_leap_year(leap_check):
    if leap_check % 4 == 0:
        if leap_check%100 == 0:
            if  leap_check%400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def months_scale(year,month):
    months_of_days=[31,29,31,30,31,30,31,31,30,31,30,31]
    #months_of_non_leap=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return months_of_days[month-1]
        
#leap_output= is_leap_year(year)        
days=months_scale(year,month)
print(days)
