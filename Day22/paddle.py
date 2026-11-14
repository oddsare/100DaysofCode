from turtle import Turtle
class Paddle(Turtle): 
    
    def __init__(self,paddle_x,paddle_y):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()

        self.goto(paddle_x,paddle_y)
        
        

    def moving_up(self):
        new_y =self.ycor() +20
        self.goto(self.xcor(), new_y)
        
    def moving_down(self):
        new_y =self.ycor() -20
        self.goto(self.xcor(), new_y)




