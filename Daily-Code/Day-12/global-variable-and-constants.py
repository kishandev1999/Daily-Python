#GLOBAL VARIABLE
enemies=1
def increase_enemies():
    global enemy_count
    enemies + 1

enemies = increase_enemies()
print(f"enemies inside function : {enemies}")
#OUTPUT:
'''
HERE YOU ARE DECLARING THE VARIABLE INSIDE THE FUNCTION AT GLOBAL LEVEL
SO, THIS ENEMIES VARIABLE WILL BE CONSIDERED AS SAME THROUGHOUT THE CODE, EVEN THOUGH IT IS INSIDE THE FUNCTION
'''



'''
IT IS NOT A GOOD PRACTICE TO DECLARE THE GLOBAL VARIABLES INSIDE THE FUNCTION
SO, USE THE RETURN FUNCTION.
'''
#INSTEAD USE THE RETURN VALUE:
enemies=1
def increase_enemies():
    print(f"enemies inside function : {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies inside function : {enemies}")

#CONSTANT
#IN PYTHON, WE CAN DECLARE THE CONSTANTS IN CAPITAL CASE
PI = 3.14159
USERNAME="kishan"
URL='http://kishandev.py.com'
PASSWORD="Angel!@!231"