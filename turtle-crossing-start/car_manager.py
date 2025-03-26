from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.All_CAR = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            new_car.goto(290, y)
            self.All_CAR.append(new_car)

    def move_cars(self):
        for car in self.All_CAR:
            car.backward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
