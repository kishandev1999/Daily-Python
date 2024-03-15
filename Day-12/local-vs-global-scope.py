########SCOPE##########

#-----LOCAL------------
portion_level=10
#THIS IS A GLOBAL VARIABLE

def drink_portion():
    #THIS IS CALL LOCAL VARIABLE
    #LOCAL SCOPE
    portion_level=2
    print(portion_level)
    
#ONCE THE FUNCTION CALLING IS COMPLETED
#THIS VALUE IS BE REMOVED
drink_portion()

print(portion_level)
#THIS WILL PRINT THE GLOBAL VARIABLE

#OUTPUT:
'''
2
10
'''

#---------GLOBAL----------
#GLOBAL VARIABLE
player_health=20

def player_rate():
    rage_level=5
    #CALLING VARIABLE DECLARED OUTSIDE THE FUNCTION
    #MEANS IT IS GLOBAL 
    print(player_health)
    
player_rate()

#OUTPUT:
#10

#THIS LOCAL AND GLOBAL SCOPE IS NOT ONLY APPLICABLE TO THE VARIABLES. BUT, ALSO WITH THE FUNCTIONS
player_haste=15
def play_game():
    def player_rate():
        health_level=5
        print(player_haste)
    
    player_rate()
    

    
    
     
