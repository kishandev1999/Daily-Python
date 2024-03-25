# Dictionaries are like key-value pairs
'''
SYNTAX:
dict ={"key1":"value1", "key2":"value2"}
'''
#KEY VALUE PAIRS ARE DECLARED WITH ":" "COLUMN"
program_dict={"Bug":"An error that prevents a program from running unexpected",
         "Function":"A piece of code that you can easily call over and over again",
         "Loop":"It will iterate the items again and again"}

#PRINTING THE VALUES IN THE DICTIONARIES
#WE WILL PRINT THE VALUES USING KEYS
#KEYS ALWAYS MUST BE IN QUOTES FOR STRINGS
print(program_dict["Bug"])

#ADDING NEW ITEMS IN THE DICTIONARY:
program_dict["data"]="a group of information"
print(program_dict)
#OUTPUT:
'''
{'Bug': 'An error that prevents a program from running unexpected', 
'Function': 'A piece of code that you can easily call over and over again', 
'Loop': 'It will iterate the items again and again', 
'data': 'a group of information'}
'''

#DECLARING EMPTY DICTIONARY
empty_dict = {}

#WIPE THE DATA IN DICTIONARY
'''
program_dict ={}
print(program_dict)
'''
#OUTPUT:
#{}

#EDIT THE ITEM IN THE DICTIONARY
program_dict["Loop"]="iterate the values given in the array or string"
print(program_dict)
#OUTPUT:
'''
{'Bug': 'An error that prevents a program from running unexpected', 
'Function': 'A piece of code that you can easily call over and over again', 
'Loop': 'iterate the values given in the array or string'}
'''


#LOOP THROUGH DICTIONARY
car_brand = { "brand": "Ford","model": "Mustang","year": 1964 }
for key in car_brand:
    print(key)
    print(car_brand[key])
    
#OUTPUT:
'''
brand
Ford
model
Mustang
year
1964
'''
