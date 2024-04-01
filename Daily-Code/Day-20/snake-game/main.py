from turtle import Screen
import time
from snake import Snake

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('coral')
screen.title('My Snake Game')
#screen.tracer(0)

#FOR PLOTTING REFERENCE :
#https://www.desmos.com/calculator/mhq4hsncnh



screen.listen()   
snake=Snake()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    #This is traces. This will update the snake moment
    screen.update()
    time.sleep(0.1)
    snake.move()
    
     
        


screen.exitonclick()