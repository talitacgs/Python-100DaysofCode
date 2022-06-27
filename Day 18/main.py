import colorgram
from turtle import Turtle, Screen
import random

rick = Turtle()
colors = colorgram.extract('jibaro.jpg.jpg', 70)
colors_rgb = []
my_screen = Screen()
my_screen.colormode(255)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new = (r, g, b)
    colors_rgb.append(new)

print(colors_rgb)

y = -150

for i in range(10):
    rick.penup()
    rick.goto(-100,y)
    for _ in range(10):
        rick.pendown()
        rick.dot(20,random.choice(colors_rgb))
        rick.penup()
        rick.forward(50)

    y+=50



my_screen.exitonclick()