#FUNCTION INPUTS:
'''
IF WE WANT TO PASS ANY VALUES IN THE FUNCTIONS
WE WILL PASS THOSE IN PARAMETERS INSIDE THE FUNCTIONS

SYNTAX:
def myfunction(something):
    do this {something}
    do that {something}
    
myfunction(that_thing)
'''
def greet_with_name(name):
    print (f"Hello, {name}")
    print(f"How are you?")
    
greet_with_name("kishan")
#or
greet_with_name(name="kishan")



def greet_with_name(name):
    print (f"Hello, {name}")
    print(f"How are you?")
    
greet_with_name("kishan")
#or
greet_with_name(name="kishan")

#here "name" is PARAMETER and "kishan" is ARGUMENT 

#POSITION VS KEYWORD ARGUMENT
def greet(name,location):
    print(f"Hello, My name is {name}")
    print(f"I'm from {location}")
    
    
greet("Kishan","India")
#OUTPUT:
'''
Hello, My name is Kishan
I'm from India
'''


greet("India", "Kishan")
#OUTPUT:
#HERE YOU CAN UNDERSTAND THE POSITIONAL ARGUMENTS
'''
Hello, My name is India
I'm from Kishan
'''


greet(name="Kishan", location="India")
#OUTPUT:
#HERE YOU CAN UNDERSTAND THE KEYWORD ARGUMENTS
'''
Hello, My name is Kishan
I'm from India
'''


greet(location="India",name="Kishan")
#OUTPUT:
#THOUGH WE CHANGE THE POSITIONS IN THE KEYWORD ARGUMENTS, THE VALUES WILL APPEND ACCORDING TO THE PARAMETER NAMES
'''
Hello, My name is Kishan
I'm from India
'''
