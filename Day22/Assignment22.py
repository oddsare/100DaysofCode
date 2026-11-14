from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
turtle = Turtle()
scoreboard = Scoreboard()
ball = Ball()
l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)





screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG")
screen.tracer(0)

screen.listen()
screen.onkey(l_paddle.moving_up,"w")
screen.onkey(l_paddle.moving_down,"s")
screen.onkey(r_paddle.moving_up,"Up")
screen.onkey(r_paddle.moving_down,"Down")


    
    




is_game_on = True
scoreboard.r_score = 0
scoreboard.l_score = 0
turtle.hideturtle()
turtle.penup()
turtle.setpos(0,300)
turtle.right(90)
turtle.pensize(5)
turtle.pendown()
turtle.pencolor("White")

for i in range(19):

    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.forward(10)  
    n= 0.1
while is_game_on:
 


    
    time.sleep(n)

    ball.move()    
    screen.update()

    
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_paddle()

    if ball.xcor() > 380:
        
        ball.rest_position()
        scoreboard.increase_l_score()
        if n > 0:
            n = max(0.0, round(n - 0.01, 4))
    if ball.xcor() < -380:
        
        ball.rest_position()
        scoreboard.increase_r_score()
        if n > 0:
            n = max(0.0, round(n - 0.01, 4))

screen.exitonclick()