from turtle import Turtle, Screen
from snake import Snake
import time

snake = Snake()
screen = Screen()
screen.setup(600,600)
screen.bgcolor("Black")
screen.title("Snake")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.snake_move()
        


screen.exitonclick()

