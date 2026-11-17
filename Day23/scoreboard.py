from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        



    def level(self,level):
        self.hideturtle()
        self.color("Black")
        self.penup()
        self.goto(-200,250)
    
        self.write(f"Level: {level}",False,"center",FONT)
        
        
    
    
    def game_over(self,level):
        self.clear()
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER",False,"center",FONT)        
