#FUNCTION WITH OUTPUTS
'''
SYNTAX:
def my_function():
    return 3*2
    
output = my_function()
#THIS WILL SHOW THE OUTPUT: 6
'''

#CHALLENGE:1
def format_function(f_name,l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
    
print(format_function("KISHAN","DEV"))
#or
output=format_function("GAME","DEVELOPER")
print(output)

#INBUILT FUNCTIONS OUTPUTS
#OUTPUT = len(data)

#MULTIPLE RETURN VALUES:

def format_function2(f_name,l_name):
    if f_name == "" or l_name == "" :
        #return
        #BY DEFAULT THIS RETURN WILL BE "none"
        return "You haven't provided any inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
    
print(format_function2(input("Enter your firstname : "),input("Enter your lastname : ")))

#OUTPUT FOR VALUES PROVIDED :
'''
Enter your firstname : kishan
Enter your lastname : dev
Kishan Dev
'''
#OUTPUT FOR NULL VALUES
'''
Enter your firstname : 
Enter your lastname : 
You haven't provided any inputs
'''




   
    