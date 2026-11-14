from turtle import Turtle,Screen

screen = Screen()
turtle = Turtle()


screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG")

turtle.penup()
turtle.setpos(0,300)
turtle.right(90)
turtle.pensize(5)
turtle.pendown()
turtle.pencolor("White")
turtle.forward(100)


screen.exitonclick()