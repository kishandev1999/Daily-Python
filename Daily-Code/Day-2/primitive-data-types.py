#DATA TYPES :

#STRING
print("Hello")
print("Hello"[0]) #output : H
print("123"+"456") #output : 123456

street_name="Abbey Road"
print(street_name[4] + street_name[7])
#output : yo

#FLOATING POINT
734_529.678 #This underscore will give for large numbers
#if you print this, this will give you the output : 734529.678
3.14159

#BOOLEAN
True
False

#EXERCICSE
two_digit_number = input() #default this type will be in string format

#Now we need to convert the digits to int to sum them
first_digit = int(two_digit_number)
second_digit = int(two_digit_number)

#Add these together
sum_of_digits = first_digit + second_digit
print(sum_of_digits)
