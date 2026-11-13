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
        self.spacing = 0
        #this range will needed to be added
        for i in range(0,n):
            self.add_snanke(self.spacing)
            

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
            
    def extend_snake():
        pass
    def add_snanke(self,spacing):
        self.square_shape = Turtle("square")
        self.square_shape.penup()
        self.square_shape.color("White")
        self.square_shape.setpos(spacing,0)
        spacing -= 21
        self.snake.append(self.square_shape)