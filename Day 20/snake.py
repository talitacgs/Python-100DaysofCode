from turtle import Turtle
from random import choice
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        x = 20
        colors = ['white','red','orange','yellow','green','blue','purple']
        self.body_pieces = []
        for _ in range(3):
            snake = Turtle(shape='square')
            snake.color(choice(colors))
            snake.penup()
            snake.goto(x, 0)
            self.body_pieces.append(snake)
            x += 20


    def move(self):

        for body_pieces_num in range(len(self.body_pieces) - 1, 0, -1):
            # The last turtle follow the turtle in front of
            new_x = self.body_pieces[body_pieces_num - 1].xcor()
            new_y = self.body_pieces[body_pieces_num - 1].ycor()
            self.body_pieces[body_pieces_num].goto(new_x, new_y)
        self.body_pieces[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.body_pieces[0].heading() != DOWN:
            self.body_pieces[0].setheading(UP)

    def down(self):
        if self.body_pieces[0].heading() != UP:
            self.body_pieces[0].setheading(DOWN)

    def left(self):
        if self.body_pieces[0].heading() != RIGHT:
            self.body_pieces[0].setheading(LEFT)

    def right(self):
        if self.body_pieces[0].heading() != LEFT:
            self.body_pieces[0].setheading(RIGHT)

