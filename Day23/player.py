from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

scoreboard = Scoreboard()
class Player(Turtle):
   
    def __init__(self):
      super().__init__()
      self.penup()
      self.goto(STARTING_POSITION)
      self.shape("turtle")
      self.setheading(90)
      self.level = 1
      
      
      
      
    

    def moving_forward(self):
        self.forward(MOVE_DISTANCE)


    def player_check_distance(self,player):
        
        if player.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.level += 1
            scoreboard.clear()
            scoreboard.level(self.level)
            return True
        else:
            scoreboard.clear()
            scoreboard.level(self.level)
            return False
            
            
            
            