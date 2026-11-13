from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
snake = Snake()
food = Food()
scorebard = Scoreboard()



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
    #collision_with_food     
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.make_square(1)
     
        scorebard.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scorebard.game_over()
        game_is_on = False
    for part_of_snake in snake.snake[1::]:

        if snake.head.distance(part_of_snake) < 10:
            game_is_on = False
            scorebard.game_over()
            

screen.exitonclick()

