from turtle import Turtle,Screen
import random
#IMPORT EXAMPLES:

'''
#IMPORT 
import turtle
tim = turtle.Turtle()
#YOU HAVE TO USE THE CLASSES IN THE MODULE IN THIS WAY.
'''


'''
#IMPORT ALL

#import turtle *   //ALL// //THIS WILL IMPORT ALL THE CLASSES IN THE MODULE//
forward(100)
turtle()

THIS IS NOT A GOOD PRACTICE TO USE. BECAUSE, INCASE WE ARE USING MANY MODULES AND IF WE USE IN THIS WAY, IT WOULD BE DIFFICULT TO KNOW WHERE
THIS FUNCTION CAME FROM!
'''

'''
#IMPORT FROM

form turtle import Turtle
tim = Turtle()
'''

'''
#IMPORT AS

#import turtle as t  //ALIASING//
For this every time you call this module, instead of using turtle.Turtle()
You can use t.Turtle()
'''

#NOTE: This turtle package is preinstalled in python version. So, no need to install separately.
#If you want to use any new MODULES. First, we need to install them.

timmy_turtle   = Turtle()
#timmy_turtle.shape('arrow')
timmy_turtle.color('red')

'''
#DRAW THE SQUARE WITH THE TURTLE:
timmy_turtle.forward(100)
timmy_turtle.left(90)
timmy_turtle.forward(100)
timmy_turtle.left(90)
timmy_turtle.forward(100)
timmy_turtle.left(90)
timmy_turtle.forward(100)
'''

#SQUARE IN LOOP FORMAT:
'''
for _ in range(4):
    timmy_turtle.forward(100)
    timmy_turtle.left(90)

#timmy_turtle.width(20)

'''

'''
#DRAW THE DASHED LINES USING THE FOR LOOP
for steps in range(10):
    if steps%2 == 0:
        timmy_turtle.color('black')
        timmy_turtle.forward(25)
    else:
        timmy_turtle.color('white')
        timmy_turtle.forward(25)
'''

#USING THE METHODS:
'''
for _ in range(15):
    timmy_turtle.forward(10)
    timmy_turtle.penup()
    timmy_turtle.forward(10)
    timmy_turtle.pendown()
'''

#DRAWING THE TRIANGLE,RECTANGLE,PENTAGON,HEXAGON......
#def instructions(angle):
#    timmy_turtle.forward(100)
#    timmy_turtle.left(360/3)
    
'''
colors=['red','green','blue','yellow','pink','purple','black','coral','cyan','gold']

def instructions(num_sides):  
    color_index=6
    angle=360/num_sides
    for _ in range(1,num_sides+1):
        timmy_turtle.forward(100)
        timmy_turtle.right(angle)
    
            
for _ in range(3,11):
    instructions(_)
    colors_rand=random.choice(colors)
    timmy_turtle.color(colors_rand)
'''

#RANDOM WALK 
'''
#colors=['Aqua','green','blue','yellow','pink','purple','black','coral','cyan','gold']
colors=['red','pink','purple','yellow','orange']
degree=[0,90,180,270]
walk=['south','east','west','north']
timmy_turtle.width(10)


while True:
    colors_rand=random.choice(colors)
    random_walk=random.choice(degree)
    timmy_turtle.forward(25)
    timmy_turtle.setheading(random_walk)
    timmy_turtle.color(colors_rand)
    
'''

timmy_turtle.circle(50)
timmy_turtle.settiltangle(30)
timmy_turtle.setposition(5,0)
timmy_turtle.circle(50)
timmy_turtle.settiltangle(60)
timmy_turtle.circle(50)
timmy_turtle.settiltangle(80)
timmy_turtle.circle(50)
timmy_turtle.settiltangle(100)

    
    
    
    
    
    
    

    


    
    
    



screen=Screen()
screen.exitonclick()