'''
#OBJECT STATE
We can use individual objects from the class.
Each will act independently

#EXAMPLE:
new_turtlemy.color = green
tommy.color = purple

- HERE, new_turtlemy property is different. Tommy property is different.
'''
from turtle import Turtle,Screen
import random
screen=Screen()


screen.setup(width=500,height=500)
user_bet=screen.textinput(title="MAKE YOUR BET!!",prompt="Who will win the race?")
colors=['yellow', 'blue', 'green', 'purple','red','pink','orange']
all_turtles=[]


y_axis=[-70,-40,-10,20,50,80,110]
for turtle_index in range(len(colors)):
    new_turtle=Turtle()
    new_turtle.color(colors[turtle_index])
    new_turtle.shape('turtle')
    new_turtle.penup()
    start_point=new_turtle.goto(-230,y_axis[turtle_index])
    all_turtles.append(new_turtle)
    
    
    
#print(all_turtles)
is_finish = True
while is_finish:
    for turtle in all_turtles:
        if turtle.xcor() < 220:
            random_distance=random.randint(1,10)
            turtle.forward(random_distance)
        else:
            winner=turtle.pencolor()
            if user_bet == winner:
                print(f"*** Congratulations ***: {winner} won the match")
            else:
                print("*** SORRY, YOU LOST ***")
                print(f"The winner is {winner}")
            is_finish=False
    





'''
yellow=Turtle()
blue=Turtle()

yellow.color('yellow')
yellow.shape('turtle')
yellow.penup()
yellow.setpos(-250,0)



blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.setpos(-250,20)
#blue.pos()
'''

screen.exitonclick()
