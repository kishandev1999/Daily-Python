#BLOCK SCOPE
game_level=3

def game():
    enemies=['zombies','skeleton','Alien']
    if game_level > 5:
        new_enemy = enemies[0]
        #IF ANY VARIABLE DECLARED IN IF BLOCK OR FOR LOOP
        #THAT IS NOT COUNT AS CREATING SEPARATE LOCAL SCOPE
        '''
        In Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.
        '''
        
    print(new_enemy)
    
game()

#OUTPUT
'''
UnboundLocalError: cannot access local variable 'new_enemy' where it is not associated with a value
'''