from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWNN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.make_square()
        self.head =self.snake[0]
        

    def make_square(self):
        spacing = 0
        for i in range(0,3):
            self.square_shape = Turtle("square")
            self.square_shape.penup()
            self.square_shape.color("White")
            self.square_shape.setpos(spacing,0)
            spacing -= 21
            self.snake.append(self.square_shape)
            

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