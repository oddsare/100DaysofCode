from turtle import Turtle, Screen
import random

colors =["Red","Blue", "Green", "Yellow", "Purple","Orange"]

is_race_on = False
all_turtles = []

def turtle_setup(turtle,color,x,y,index_of_turtle):
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(colors[index_of_turtle])
    turtle.goto(x,y)
    return turtle
    
n = 125 
for i in range(0,6):
    turtle1 = Turtle()
    turtle1 =turtle_setup(turtle1,colors[0],-230,n,i)
    n -= 50    
    all_turtles.append(turtle1)
    
screen = Screen()
screen.setup(500,400)
#width  is 500 
# height is 400

user_bet = screen.textinput("Make a Bet","Who do you bet on? Red/Blue/Green/Yellow/Orange or Purple").lower()


if user_bet:
    is_race_on = True 

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor().lower()
            if winning_color == user_bet:
                print(f"You win, you guess the correct color {winning_color}")
            else:
                print(f"You lost, you did not guess the correct color it was: {winning_color}")
            is_race_on = False
        ran_distance = random.randint(0,10)
        turtle.forward(ran_distance)

screen.exitonclick()