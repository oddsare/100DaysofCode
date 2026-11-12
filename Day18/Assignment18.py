from turtle import Turtle, Screen
import turtle
import random
###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
turtle.colormode(255) 
tim = Turtle()



def movement(lat,long,color):
    new_color =random.randint(2,(len(color)-1))
    
    tim.teleport(lat,long)
    tim.dot(20,color[new_color])

tim.speed("fast")
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    
    new_color = (r,g,b)
    rgb_colors.append(new_color)

lat = -225
long = -225
for i in range(10):
    lat= -225
    for j in range(10):
        movement(lat,long,rgb_colors)
        lat += 50
        
    long += 50


screen = Screen()
screen.exitonclick()