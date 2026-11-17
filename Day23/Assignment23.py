import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()
speed = 10
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkeypress(player.moving_forward,"Up")


car_manager = CarManager()



game_is_on = True
while game_is_on:
    

       
        
    player.player_check_distance(player)
    time.sleep(0.1)
    screen.update()
    car_manager.car()
    if player.player_check_distance(player) == True:
        car_manager.move_forward(speed)
        speed += 10
    else:
        car_manager.move_forward(speed)
    
    for a_car in (car_manager.group_cars):
                
        if player.distance(a_car) < 20:
            scoreboard.game_over(player.level)
            game_is_on = False

   
screen.exitonclick()