from turtle import Turtle
SCORE_BOARD_FONT = "imago bold"
SCORE_BOARD_FONT_BOLDNESS = "bold"
SCORE_BOARD_FONT_SIZE = 12
SCOREBOARD_LAYOUT = "center"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
            
        self.high_score = int(self.high_score)
        self.penup()
        self.speed(10)
        self.goto(0,280)
        self.color("White")
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False,SCOREBOARD_LAYOUT,font=(SCORE_BOARD_FONT,SCORE_BOARD_FONT_SIZE,SCORE_BOARD_FONT_BOLDNESS))
    def increase_score(self):
    
        self.score += 1
        self.update_scoreboard()
       
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as file:
                        file.write((str(self.high_score)))
        self.score = 0
        self.update_scoreboard()
             
       
       
       
        
    #def game_over(self):
        #self.goto(0,0)
        #self.color("White")
        
        #self.write(f"GAME OVER", False,SCOREBOARD_LAYOUT,font=(SCORE_BOARD_FONT,SCORE_BOARD_FONT_SIZE,SCORE_BOARD_FONT_BOLDNESS))
        
        
        