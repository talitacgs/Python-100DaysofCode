from turtle import Turtle
import random

BALL_SPEED = 0.5
ANGLE = random.randint(0, 360)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 0.07
        self.shape('circle')
        self.penup()
        self.color('white')


    def move_ball(self):
        global ANGLE
        self.setheading(ANGLE)
        # Avoids an infinite loop in case the angle is 90 or 270 degrees.
        while 100 >= ANGLE >= 80 or 280 >= ANGLE >= 260:
            ANGLE = random.randint(0, 360)
            self.setheading(ANGLE)
        self.forward(self.ball_speed)

    def bounce(self):
        global ANGLE
        # Add physics to the bounce. Returns the explementary angle of the ball.
        ANGLE = 360-ANGLE
        self.setheading(ANGLE)
        self.forward(self.ball_speed)

    def paddle_bounce(self):
        global ANGLE
        # Add physics to the bounce. Returns the supplementary angle of the ball.
        ANGLE = 180-ANGLE
        self.setheading(ANGLE)
        self.ball_speed = self.ball_speed * 1.05
        self.forward(self.ball_speed)

    def reset_ball(self):
        global ANGLE
        self.goto(0, 0)
        ANGLE = random.randint(0, 360)
        self.move_ball()

    def reset_speed(self):
        self.ball_speed = 0.07

