from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('coral')
screen.title('My Snake Game')
#screen.tracer(0)

#FOR PLOTTING REFERENCE :
#https://www.desmos.com/calculator/mhq4hsncnh



screen.listen()   
snake=Snake()
food=Food()
scoreboard=Scoreboard()
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
    
    #DETECT COLLISION WITH FOOD
    #THROUGH DISTANCE METHOD
    if snake.head.distance(food) < 15 :
        #print("Nom nom niom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #HITTING THE WALL    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
    #DETECT THE TAIL
    for segment in snake.snake_initial_obj: # segment in snake.snake_initial_obj[1:]
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
     
        


screen.exitonclick()