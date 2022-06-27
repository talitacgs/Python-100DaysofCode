import random
from turtle import Turtle


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()

    def create_car(self):
        # Filters the number of cars being created.
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape='square')
            car.shapesize(1, 2)
            car.penup()
            car.goto(330, random.randrange(-160, 280, 10))
            car.color(int(random.randint(1, 255)), int(random.randint(1, 255)), int(random.randint(1, 255)))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(STARTING_MOVE_DISTANCE)

    @staticmethod
    def level_up():
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
