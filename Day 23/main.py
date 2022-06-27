from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.colormode(255)
screen.title('Crossing')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.up, 'Up')

is_on = True

while is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Successful run events.
    if player.finish():
        player.finish()
        car_manager.level_up()
        scoreboard.add_score()

    # Collision detection.
    for car in car_manager.cars:
        if car.distance(player) < 20:
            is_on = False
            scoreboard.lost()

screen.exitonclick()
