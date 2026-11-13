from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWNN = 270
LEFT = 180
RIGHT = 0
N= 3


class Snake:

    def __init__(self):
        self.snake = []
        self.make_square(N)
        self.head =self.snake[0]
        

    def make_square(self,n):
   
        #this range will needed to be added
        for i in range(0,n):
            self.add_snanke(-20*i,0)
            

    def snake_move(self):
        for seg in range(len(self.snake)-1,0,-1):
            newx= self.snake[seg-1].xcor()
            newy = self.snake[seg-1].ycor()
            self.snake[seg].goto(newx,newy)
                
                
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWNN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWNN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    def extend_snake(self):
        tail =self.snake[-1]
        self.add_snanke(tail.xcor(),tail.ycor())
    def add_snanke(self,x,y):
        self.square_shape = Turtle("square")
        self.square_shape.penup()
        self.square_shape.color("White")
        self.square_shape.setpos(x,y)
        self.snake.append(self.square_shape)