#CREATING THE CLASS
class User():
    def __init__(self, user_id, username):
        print("This is the User call")
        #EVERYTIME WHEN CONSTRUCTION HAPPENED, IT WILL PRINT THE ABOVE STATEMENT
        
        #ATTRIBUTES:
        '''
        EXAMPLE
        class Car:
            def __init__(self,seats):
                self.seats= seats
        -----------------------------
        #CALLING CONSTRUCTOR:
        my_car = Car(5)
        
        #IT WILL BE THE SAME AS CREATE OBJECTS AND CALLING AS BELOW:
        my_car= Car()
        my_car.seats(5)
        '''
        #CREATING ATTRIBUTES
        self.id = user_id
        self.username = username
        self.followers =0
        self.following=0
      
        
    #METHODS
    '''
    #DECLARING THE METHOD
    class Car:
        def enter_race_mode():
            self.seats=2
            
    #CALLING THE METHOD:
    my_car=Car()
    my_car.enter_race_mode()       
    '''
    #CREATING THE METHODS:
    def follow(self, user):
        user.followers +=1
        self.following +=1



'''
#CREATING AN OBJECT
user1=User()
'''

#CALLING THE CLASS WITH ATTRIBUTES
user1=User("001","Kishan")
user2=User("002", "Dev")
print(user2.username)
#output
#Dev

#DECLARING THE ATTRIBUTES:
'''
user1.id="001"
user1.username="Kishan"
print(user1.username)
#OUTPUT 
#KISHAN

SO, HERE PROVIDING THE ATTRIBUTES IS A LONG PROCEDURE, IF WE HAVE MORE
HENCE, WE ARE CHOOSING "CONSTRUCTOR"
EXAMPLE:
class Car():
    def __init__(self):
        #INITIALIZE YOUR ATTRIBUTES
'''

#NOTE:
#THE CLASS MUST BE DEFINED IN PASCALCASE:
'''
EXAMPLE:
User
CarCameraModule
CoffeeMaker
ChessDashboard
'''


#CALLING THE METHODS:
user1.follow(user2)
print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)

#OUTPUT
'''
This is the User call
This is the User call
Dev
0
1
1
0
'''
