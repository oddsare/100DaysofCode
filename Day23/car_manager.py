from turtle import Turtle
from player import Player
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        
        self.group_cars = []
        
        
    def car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
        
            the_car = Turtle()
            the_car.penup()
            the_car.shape("square")
            the_car.shapesize(1,1.5)
            the_car.setheading(180)
            the_car.color(random.choice(COLORS))
            the_car.goto(300,random.randint(-250,250))
            
            self.group_cars.append(the_car)
        
    def move_forward(self,the_player):
        speed = STARTING_MOVE_DISTANCE
        if the_player.level > 1:
            speed += MOVE_INCREMENT
        
        for a_car in (self.group_cars):
            
            a_car.forward(speed)



            
            