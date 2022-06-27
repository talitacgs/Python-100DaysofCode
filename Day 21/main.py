import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.colormode(255)
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.size[0].distance(food) < 30:
        food.refresh()
        scoreboard.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.size[0].xcor() > 280 or snake.size[0].xcor() < -280 or \
            snake.size[0].ycor() > 280 or snake.size[0].ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for size in snake.size[1:]:
        if snake.size[0].distance(size) < 10:
            scoreboard.reset_score()
            snake.reset_snake()




screen.exitonclick()
