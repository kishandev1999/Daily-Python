from turtle import Turtle

snake_initial_pos=[(0,0),(-6,0),(-12,0)]

class  Snake():
    def __init__(self):
      self.snake_initial_obj=[]
      #THIS WILL CREATE THIS METHOD AUTOMATICALLY, WHEN YOU CALL THE SNAKE CLASS
      self.create_snake()
      self.head = self.snake_initial_obj[0]
      
        
    def create_snake(self):
        #snake_initial_obj=[]
        for i in snake_initial_pos:
            self.add_segment(i)
    
    def add_segment(self, i):
        snake_grow_part=Turtle()
        snake_grow_part.color('white')
        snake_grow_part.shape('square')
        snake_grow_part.penup()
        snake_grow_part.goto(i)
        self.snake_initial_obj.append(snake_grow_part)
    
    def extend(self):
        #Add new segment to snake
        self.add_segment(self.snake_initial_obj[-1].position())
    
    def move(self):
        for seg_num in range(len(self.snake_initial_obj)-1,0,-1):
            new_x = self.snake_initial_obj[seg_num-1].xcor()
            new_y = self.snake_initial_obj[seg_num-1].ycor()
            self.snake_initial_obj[seg_num].goto(new_x,new_y)
        self.snake_initial_obj[0].forward(20)  
        
    def up(self):
        self.snake_initial_obj[0].setheading(90)
        
    def down(self):
        self.snake_initial_obj[0].setheading(270)
        
    def left(self):
        self.snake_initial_obj[0].setheading(180)
        
    def right(self):
        self.snake_initial_obj[0].setheading(0)
        
        
        
        

        

    
    
    
#for segment in snake_initial_obj:
   