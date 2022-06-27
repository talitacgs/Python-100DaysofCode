from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.color(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
        self.penup()
        self.goto(ran_x, ran_y)

