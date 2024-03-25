#ERRORS
len(23456)
#This will leave an error, because this len function is only for string

num_char = len(input("What is your name?"))
print("Your name has" + num_char + "characters")

#TYPE
#if you want to know what is the type of the data or variable use this type function
print(type(num_char))

#TYPE CONVERSION
str(your_variable_name)
int(your_variable_name)

#EXAMPLE CASE FOR TYPE CONVERSION:
num_char = len(input("what is your name?"))
#This will count the characters of your string you provide. This value will be in int type
new_num_char = str(num_char)
#The above will convert int data type to string
print("Your name is " + new_num_char + "characters")
#This is concatenate the value in between the strings.

#FLOAT CONVERSION
a=float(123)
print(type(a))
print(70+float("100.5")) #output = 170.5


