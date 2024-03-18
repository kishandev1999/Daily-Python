from turtle import Turtle,Screen

#OBJECT = CLASS
'''
EXAMPLE:
say!!! car is an OBJECT
OBJECT = CLASS 
car    = CarBlueprint()

say!!! #OBJECT ATTRIBUTES
car has attributes : {speed =0 and fuel=32}
When it comes to accessing these attributes in a way : 
car.speed
//object.attribute//

say!!! #OBJECT METHODS
car has methods: (mentioned 2)
1. def move():
    speed=60
2. def stop():
    speed=0
When it comes to accessing these attributes in a way : 
car.stop()
//object.method()//
'''
timmy   = Turtle()
#object   class

print(timmy)

#below 3 are examples for calling methods
timmy.shape("turtle")
#This will change the arrow to turtle shape

timmy.color("coral")
#This will change the color of turtle to coral

timmy.forward(100)
#This will move turtle forward and draw the straight line

#OBJECT ATTRIBUTE
my_screen=Screen()
print(my_screen.canvheight)
#     object.attribute       
#Here we also printed the screen height
#output : 300


#OBJECT METHOD()
my_screen.exitonclick()
#OUTPUT:
#YOU'LL SEE A WINDOW-POPUP AND IT WILL CLOSE WHEN YOU CLICK ON IT

#REFERENCE:
#https://docs.python.org/3/library/turtle.html

#FOR COLORS:
#https://cs111.wellesley.edu/reference/colors
