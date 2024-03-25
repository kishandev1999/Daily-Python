'''
import colorgram
from turtle import Turtle, Screen
rgb_colors=[]
colors = colorgram.extract('Z:\Daily-Python\Day-18\Hist Painting\dots-image.jpg',10)
#print(colors)

for color in colors:
    r= color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
    
#print(rgb_colors)

color_list=[(254, 254, 253), (252, 240, 244), (246, 253, 249), (250, 139, 54), (50, 171, 91), (120, 185, 140), (247, 75, 110), (246, 222, 62), (248, 77, 51), (120, 120, 67)]
    
timmy=Turtle()
#timmy.forward(100)
#timmy.home()
#position=timmy.pos()
timmy.goto(-200,-300)
#print(position)


screen=Screen()
screen.exitonclick()
#screen.screensize(10,10)
'''
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()