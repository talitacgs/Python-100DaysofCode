from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.colormode(255)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score_r = Score(150, 250)
score_l = Score(-150, 250)

screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

is_on = True
while is_on:
    screen.update()
    ball.move_ball()

    # Detects collision with up and bottom walls.
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()

    # Detects collision with the paddles.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # Detects when the paddle misses the ball.
    if ball.xcor() > 350:
        ball.reset_ball()
        score_l.add_score()
        ball.reset_speed()
    if ball.xcor() < -350:
        ball.reset_ball()
        score_r.add_score()
        ball.reset_speed()

screen.exitonclick()
